from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMenu
from PySide6.QtGui import QImage, QPixmap, QColor
from PySide6.QtCore import QTimer, QThread, Signal, QObject, QPoint, Qt
from ui.home import Ui_MainWindow
import sys
import os
import json
import cv2
from navGPT.yolo import YOLO

class MainWindow(QMainWindow, Ui_MainWindow):
    main2yolo_begin_sgl = Signal()  # The main window sends an execution signal to the yolo instance

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground)  # rounded transparent
        self.setWindowFlags(Qt.FramelessWindowHint)  # Set window flag: hide window borders
        self.close_sf.clicked.connect(self.close)

        self.status_bar.setMaximumWidth(860)

        # read model folder
        self.onnx_list = os.listdir('./models')
        self.onnx_list = [file for file in self.onnx_list if file.endswith('.onnx')]
        self.onnx_list.sort(key=lambda x: os.path.getsize('./models/' + x))  # sort by file size
        self.yoloModel_CB.clear()
        self.yoloModel_CB.addItems(self.onnx_list)
        self.Qtimer_ModelBox = QTimer(self)  # Timer: Monitor model file changes every 2 seconds
        self.Qtimer_ModelBox.timeout.connect(self.ModelBoxRefre)
        self.Qtimer_ModelBox.start(2000)

        self.label_10.clear() # image output

        self.iou_thres = 0.45            # iou
        self.conf_thres = 0.3           # conf

        self.iou_spinbox.setValue(self.iou_thres)
        self.iou_slider.setValue(int(self.iou_thres * 100))
        self.conf_spinbox.setValue(self.conf_thres)
        self.conf_slider.setValue(int(self.conf_thres * 100))

        # Model parameters
        self.yoloModel_CB.currentTextChanged.connect(self.change_model)
        self.iou_spinbox.valueChanged.connect(lambda x: self.change_val(x, 'iou_spinbox'))  # iou box
        self.iou_slider.valueChanged.connect(lambda x: self.change_val(x, 'iou_slider'))  # iou scroll bar
        self.conf_spinbox.valueChanged.connect(lambda x: self.change_val(x, 'conf_spinbox'))  # conf box
        self.conf_slider.valueChanged.connect(lambda x: self.change_val(x, 'conf_slider'))  # conf scroll bar

        self.select_model = self.yoloModel_CB.currentText()  # default model

        self.yolo_predict = YOLO(self.conf_thres, self.iou_thres)

        self.yolo_thread = QThread()
        self.yolo_predict.onnx_model = "./models/%s" % self.select_model

        # Prompt window initialization
        self.modelOutput_QL.setText(self.select_model)
        self.RobotOutput_QL.clear()
        self.modelLoco_TE.clear()
        self.modelLoco_TE.setAlignment(Qt.AlignCenter)
        self.SensorOutput_TE.clear()
        self.SensorOutput_TE.setAlignment(Qt.AlignCenter)
        # Select detection source
        self.yoloFile_QB.clicked.connect(self.open_src_file)  # select local file

        # start testing button
        self.yoloDetect_QB.clicked.connect(self.detect)  # pause/start

        self.yolo_predict.moveToThread(self.yolo_thread)

        self.yolo_predict.yolo2main_res_img.connect(lambda x: self.show_image(x, self.label_10))
        self.yolo_predict.yolo2main_status_msg.connect(lambda x: self.show_status(x))
        self.yolo_predict.yolo2main_robot_num.connect(lambda x: self.RobotOutput_QL.setText(str(x)))
        self.yolo_predict.yolo2main_loco.connect(lambda x: self.modelLoco_TE.setText(x))
        self.yolo_predict.yolo2main_sensor.connect(lambda x: self.SensorOutput_TE.setText(x))

        self.main2yolo_begin_sgl.connect(self.yolo_predict.run)
        # select local file

    def open_src_file(self):
        config_file = 'config/fold.json'
        config = json.load(open(config_file, 'r', encoding='utf-8'))
        open_fold = config['open_fold']
        if not os.path.exists(open_fold):
            open_fold = os.getcwd()
        name, _ = QFileDialog.getOpenFileName(self, 'image', open_fold,
                                              "Pic File(*.jpg *.png)")
        if name:
            self.yolo_predict.input_image = name
            self.show_status('Load File：{}'.format(os.path.basename(name)))
            config['open_fold'] = os.path.dirname(name)
            config_json = json.dumps(config, ensure_ascii=False, indent=2)
            with open(config_file, 'w', encoding='utf-8') as f:
                f.write(config_json)

            self.show_image(cv2.imread(name), self.label_10)
            self.RobotOutput_QL.clear()
            self.modelLoco_TE.clear()
            self.modelLoco_TE.setAlignment(Qt.AlignCenter)
            self.SensorOutput_TE.clear()
            self.SensorOutput_TE.setAlignment(Qt.AlignCenter)
            # self.stop()

        # Control start/pause
    def detect(self):
        if self.yolo_predict.input_image == '':
            self.show_status('Please select a media source before starting detection...')
        else:
            self.show_status('Detecting...')
            if not self.yolo_thread.isRunning():
                self.yolo_thread.start()
                self.main2yolo_begin_sgl.emit()


    # Cycle monitoring model file changes
    def ModelBoxRefre(self):
        onnx_list = os.listdir('./models')
        onnx_list = [file for file in onnx_list if file.endswith('.onnx')]
        onnx_list.sort(key=lambda x: os.path.getsize('./models/' + x))
        # It must be sorted before comparing, otherwise the list will be refreshed all the time
        if onnx_list != self.onnx_list:
            self.onnx_list = onnx_list
            self.model_box.clear()
            self.model_box.addItems(self.onnx_list)


    # bottom status bar information
    def show_status(self, msg):
        self.status_bar.setText(msg)
        if msg == 'Detection completed':
            if self.yolo_thread.isRunning():
                self.yolo_thread.quit()  # end process

        # elif msg == 'Detection terminated!':
        #     self.save_res_button.setEnabled(True)
        #     self.save_txt_button.setEnabled(True)
        #     self.run_button.setChecked(False)
        #     self.progress_bar.setValue(0)
        #     if self.yolo_thread.isRunning():
        #         self.yolo_thread.quit()  # end process
        #     self.pre_video.clear()  # clear image display
        #     self.res_video.clear()
        #     self.Class_num.setText('--')
        #     self.Target_num.setText('--')

        # Change detection parameters
    def change_val(self, x, flag):
        if flag == 'iou_spinbox':
            self.iou_slider.setValue(int(x * 100))  # The box value changes, changing the slider
        elif flag == 'iou_slider':
            self.iou_spinbox.setValue(x / 100)  # The slider value changes, changing the box
            self.show_status('IOU Threshold: %s' % str(x / 100))
            self.yolo_predict.iou_thres = x / 100
        elif flag == 'conf_spinbox':
            self.conf_slider.setValue(int(x * 100))
        elif flag == 'conf_slider':
            self.conf_spinbox.setValue(x / 100)
            self.show_status('Conf Threshold: %s' % str(x / 100))
            self.yolo_predict.confidence_thres = x / 100

        # change model
    def change_model(self, x):
        self.select_model = self.model_box.currentText()
        self.yolo_predict.new_model_name = "./models/%s" % self.select_model
        self.show_status('Change Model：%s' % self.select_model)
        self.Model_name.setText(self.select_model)

        # The main window displays the original image and detection results
    @staticmethod
    def show_image(img_src, label):
        try:
            ih, iw, _ = img_src.shape
            w = label.geometry().width()
            h = label.geometry().height()
            # keep the original data ratio
            if iw / w > ih / h:
                scal = w / iw
                nw = w
                nh = int(scal * ih)
                img_src_ = cv2.resize(img_src, (nw, nh))

            else:
                scal = h / ih
                nw = int(scal * iw)
                nh = h
                img_src_ = cv2.resize(img_src, (nw, nh))

            frame = cv2.cvtColor(img_src_, cv2.COLOR_BGR2RGB)
            img = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[2] * frame.shape[1],
                         QImage.Format_RGB888)
            label.setPixmap(QPixmap.fromImage(img))
            label.setAlignment(Qt.AlignCenter)

        except Exception as e:
            print(repr(e))

    def show_loco(self, val):
        for line in val:
            self.modelLoco_TE.appendRow(line)







    def close(self):
        sys.exit(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Home = MainWindow()
    Home.show()
    sys.exit(app.exec())