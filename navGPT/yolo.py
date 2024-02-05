import argparse

import cv2
import numpy as np
import onnxruntime as ort
from PySide6.QtCore import QObject, Signal
from utils.helper import yaml_load

class YOLO(QObject):
    """YOLOv8 object detection model class for handling inference and visualization."""
    yolo2main_pre_img = Signal(np.ndarray)  # raw image signal
    yolo2main_res_img = Signal(np.ndarray)  # test result signal
    yolo2main_status_msg = Signal(str)  # Detecting/pausing/stopping/testing complete/error reporting signal
    yolo2main_labels = Signal(dict)  # Detected target results (number of each category)
    yolo2main_progress = Signal(int)  # Completeness
    yolo2main_robot_num = Signal(int)  # Number of robot detected
    yolo2main_loco = Signal(str)  # Types of locomotion
    yolo2main_sensor = Signal(str)  # Types of perception sensor

    def __init__(self, conf, iou):
        """
        Initializes an instance of the YOLOv8 class.
        Args:
            onnx_model: Path to the ONNX model.
            input_image: Path to the input image.
            confidence_thres: Confidence threshold for filtering detections.
            iou_thres: IoU (Intersection over Union) threshold for non-maximum suppression.
        """
        QObject.__init__(self)

        #  onnx_model, input_image, confidence_thres, iou_thres

        self.labels_dict = {}  # return a dictionary of results
        self.progress_value = 0  # progress bar

        self.onnx_model = None
        self.input_image = ''
        self.confidence_thres = conf
        self.iou_thres = iou
        # Load the class names from the COCO dataset
        self.classes = yaml_load('config/navgpt.yaml')['names']

        # Generate a color palette for the classes
        # self.color_palette = np.random.uniform(0, 255, size=(len(self.classes), 3))
        self.color_palette = np.array([[118.0, 215.0, 196.0], [174.0, 214.0, 241.0], [195.0, 155.0, 211.0], [249.0, 231.0, 159.0], [174.0, 182.0, 191.0], [241.0, 148.0, 138.0]])

        self.save_res = False
        self.save_txt = False

    def run(self):
        try:
            # Check save path/label
            # if self.save_res or self.save_txt:
            #     (self.save_dir / 'labels' if self.save_txt else self.save_dir).mkdir(parents=True, exist_ok=True)
            output_image = self.main()
            self.yolo2main_res_img.emit(output_image)  # after detection
            self.yolo2main_status_msg.emit('Detection completed')
        except Exception as e:
            pass
            print(e)
            self.yolo2main_status_msg.emit('%s' % e)



    def draw_detections(self, img, box, score, class_id):
        """
        Draws bounding boxes and labels on the input image based on the detected objects.

        Args:
            img: The input image to draw detections on.
            box: Detected bounding box.
            score: Corresponding detection score.
            class_id: Class ID for the detected object.

        Returns:
            None
        """

        # Extract the coordinates of the bounding box
        x1, y1, w, h = box

        # Retrieve the color for the class ID
        color = self.color_palette[class_id]

        # Draw the bounding box on the image
        cv2.rectangle(img, (int(x1), int(y1)), (int(x1 + w), int(y1 + h)), color, 2)

        # Create the label text with class name and score
        label = f'{self.classes[class_id]}: {score:.2f}'

        # Calculate the dimensions of the label text
        (label_width, label_height), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)

        # Calculate the position of the label text
        label_x = x1
        label_y = y1 - 10 if y1 - 10 > label_height else y1 + 10

        # Draw a filled rectangle as the background for the label text
        cv2.rectangle(img, (label_x, label_y - label_height), (label_x + label_width, label_y + label_height), color,
                      cv2.FILLED)

        # Draw the label text on the image
        cv2.putText(img, label, (label_x, label_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

    def preprocess(self):
        """
        Preprocesses the input image before performing inference.

        Returns:
            image_data: Preprocessed image data ready for inference.
        """
        # Read the input image using OpenCV
        self.img = cv2.imread(self.input_image)

        # Get the height and width of the input image
        self.img_height, self.img_width = self.img.shape[:2]

        # Convert the image color space from BGR to RGB
        img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

        # Resize the image to match the input shape
        img = cv2.resize(img, (self.input_width, self.input_height))

        # Normalize the image data by dividing it by 255.0
        image_data = np.array(img) / 255.0

        # Transpose the image to have the channel dimension as the first dimension
        image_data = np.transpose(image_data, (2, 0, 1))  # Channel first

        # Expand the dimensions of the image data to match the expected input shape
        image_data = np.expand_dims(image_data, axis=0).astype(np.float32)

        # Return the preprocessed image data
        return image_data

    def postprocess(self, input_image, output):
        """
        Performs post-processing on the model's output to extract bounding boxes, scores, and class IDs.

        Args:
            input_image (numpy.ndarray): The input image.
            output (numpy.ndarray): The output of the model.

        Returns:
            numpy.ndarray: The input image with detections drawn on it.
        """

        # Transpose and squeeze the output to match the expected shape
        outputs = np.transpose(np.squeeze(output[0]))

        # Get the number of rows in the outputs array
        rows = outputs.shape[0]

        # Lists to store the bounding boxes, scores, and class IDs of the detections
        boxes = []
        scores = []
        class_ids = []

        robot_num = 0
        cases = ["2D LiDAR", "3D LiDAR", "Legged Robot", "Stereo Camera", "UAV", "UGV"]

        loco = []
        sensor = []
        loco_str = ""
        sensor_str = ""

        # Calculate the scaling factors for the bounding box coordinates
        x_factor = self.img_width / self.input_width
        y_factor = self.img_height / self.input_height

        # Iterate over each row in the outputs array
        for i in range(rows):
            # Extract the class scores from the current row
            classes_scores = outputs[i][4:]

            # Find the maximum score among the class scores
            max_score = np.amax(classes_scores)

            # If the maximum score is above the confidence threshold
            if max_score >= self.confidence_thres:
                # Get the class ID with the highest score
                class_id = np.argmax(classes_scores)

                # Extract the bounding box coordinates from the current row
                x, y, w, h = outputs[i][0], outputs[i][1], outputs[i][2], outputs[i][3]

                # Calculate the scaled coordinates of the bounding box
                left = int((x - w / 2) * x_factor)
                top = int((y - h / 2) * y_factor)
                width = int(w * x_factor)
                height = int(h * y_factor)

                # Add the class ID, score, and box coordinates to the respective lists
                class_ids.append(class_id)
                scores.append(max_score)
                boxes.append([left, top, width, height])

        # Apply non-maximum suppression to filter out overlapping bounding boxes
        indices = cv2.dnn.NMSBoxes(boxes, scores, self.confidence_thres, self.iou_thres)

        # Iterate over the selected indices after non-maximum suppression
        for i in indices:
            # Get the box, score, and class ID corresponding to the index
            box = boxes[i]
            score = scores[i]
            class_id = class_ids[i]

            if class_id in [2, 4, 5]:
                robot_num += 1;
                if cases[class_id] not in loco:
                    loco.append(cases[class_id])
                    loco_str += cases[class_id]
                    loco_str += "\n"

            if class_id in [0, 1, 3]:
                if cases[class_id] not in sensor:
                    sensor.append(cases[class_id])
                    sensor_str += cases[class_id]
                    sensor_str += "\n"

            # Draw the detection on the input image
            self.draw_detections(input_image, box, score, class_id)

        self.yolo2main_robot_num.emit(robot_num)
        self.yolo2main_loco.emit(loco_str)
        self.yolo2main_sensor.emit(sensor_str)
        # Return the modified input image
        return input_image

    def main(self):
        """
        Performs inference using an ONNX model and returns the output image with drawn detections.

        Returns:
            output_img: The output image with drawn detections.
        """
        # Create an inference session using the ONNX model and specify execution providers
        session = ort.InferenceSession(self.onnx_model, providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])

        # Get the model inputs
        model_inputs = session.get_inputs()

        # Store the shape of the input for later use
        input_shape = model_inputs[0].shape
        self.input_width = input_shape[2]
        self.input_height = input_shape[3]

        # Preprocess the image data
        img_data = self.preprocess()

        # Run inference using the preprocessed image data
        outputs = session.run(None, {model_inputs[0].name: img_data})

        # Perform post-processing on the outputs to obtain output image.
        return self.postprocess(self.img, outputs)  # output image