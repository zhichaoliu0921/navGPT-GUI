from PySide6.QtCore import QObject, Signal
import base64
import requests

class GPT(QObject):
    gpt_status_msg = Signal(str)  # Status reporting signal
    gpt_response = Signal(str) # Output signal

    def __init__(self):
        """
        Initializes an instance of the YOLOv8 class.
        Args:
            onnx_model: Path to the ONNX model.
            input_image: Path to the input image.
            confidence_thres: Confidence threshold for filtering detections.
            iou_thres: IoU (Intersection over Union) threshold for non-maximum suppression.
        """
        QObject.__init__(self)
        self.openai = None
        self.model = None

        self.system_prompt = None
        self.user_prompt = None

        self.output_str = ''

        self.image_path = None

    def encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def run(self):
        if self.openai is None or self.model is None:
            return

        if self.system_prompt is None and self.user_prompt is None:
            self.gpt_status_msg.emit('Please enter your prompts...')
        else:

            try:
                self.output_str = ''
                self.gpt_status_msg.emit('Query sent. Waiting for response...')
                response = self.openai.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "system",
                            "content": self.system_prompt
                        },
                        {
                            "role": "user",
                            "content": self.user_prompt
                        }
                    ],
                    temperature=0.7,
                    max_tokens=4096,
                    top_p=1
                )
                self.output_str += '\n=========================\nYou:\n'
                self.output_str += self.system_prompt
                self.output_str += '. '
                self.output_str += self.user_prompt
                self.output_str += '.\n\n'
                self.output_str += 'LLM:\n'
                self.output_str += response.choices[0].message.content
                self.output_str += '\n'
                self.gpt_response.emit(self.output_str)
                self.gpt_status_msg.emit('Query completed.')
                self.system_prompt = None
                self.user_prompt = None
            except Exception as e:
                self.system_prompt = None
                self.user_prompt = None
                print(e)
                self.gpt_status_msg.emit('%s' % e)


    def run_image(self):
        if self.openai is None or self.model is None:
            self.gpt_status_msg.emit('Please validate your API key...')
            return

        if self.model != "gpt-4-vision-preview":
            self.gpt_status_msg.emit('Please select GPT 4 Preview model...')
            return

        if self.image_path is None:
            self.gpt_status_msg.emit('Please choose your image...')
            return

        if self.system_prompt is None and self.user_prompt is None:
            self.gpt_status_msg.emit('Please enter your prompts...')
            return

        try:
            # Getting the base64 string
            base64_image = self.encode_image(self.image_path)

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.openai.api_key}"
            }

            payload = {
                "model": "gpt-4-vision-preview",
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": self.user_prompt
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ],
                "max_tokens": 300
            }

            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

            self.output_str += '\n=========================\nYou:\n'
            self.output_str += self.system_prompt
            self.output_str += '. '
            self.output_str += self.user_prompt
            self.output_str += '.\n\n'
            self.output_str += 'LLM:\n'
            self.output_str += response.json()['choices'][0]['message']['content']
            self.output_str += '\n'
            self.gpt_response.emit(self.output_str)
            self.gpt_status_msg.emit('Query completed.')
            self.system_prompt = None
            self.user_prompt = None
            self.image_path = None

        except Exception as e:
            self.system_prompt = None
            self.user_prompt = None
            print(e)
            self.gpt_status_msg.emit('%s' % e)






