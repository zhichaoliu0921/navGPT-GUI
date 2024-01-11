from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMenu
from PySide6.QtGui import QImage, QPixmap, QColor
from PySide6.QtCore import QTimer, QThread, Signal, QObject, QPoint, Qt
from ui.home import Ui_MainWindow
import sys
import os
import json


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground)  # rounded transparent
        self.setWindowFlags(Qt.FramelessWindowHint)  # Set window flag: hide window borders
        self.close_sf.clicked.connect(self.close)

        # read model folder
        self.pt_list = os.listdir('./models')
        self.pt_list = [file for file in self.pt_list if file.endswith('.pt')]
        self.pt_list.sort(key=lambda x: os.path.getsize('./models/' + x))  # sort by file size
        self.yoloModel_CB.clear()
        self.yoloModel_CB.addItems(self.pt_list)
        self.Qtimer_ModelBox = QTimer(self)  # Timer: Monitor model file changes every 2 seconds
        self.Qtimer_ModelBox.timeout.connect(self.ModelBoxRefre)
        self.Qtimer_ModelBox.start(2000)

        # Model parameters
        self.yoloModel_CB.currentTextChanged.connect(self.change_model)
        self.iou_spinbox.valueChanged.connect(lambda x: self.change_val(x, 'iou_spinbox'))  # iou box
        self.iou_slider.valueChanged.connect(lambda x: self.change_val(x, 'iou_slider'))  # iou scroll bar
        self.conf_spinbox.valueChanged.connect(lambda x: self.change_val(x, 'conf_spinbox'))  # conf box
        self.conf_slider.valueChanged.connect(lambda x: self.change_val(x, 'conf_slider'))  # conf scroll bar

        self.select_model = self.yoloModel_CB.currentText()  # default model


        # Prompt window initialization
        self.modelOutput_QL.setText(self.select_model)
        self.RobotOutput_QL.setText('--')
        self.modelLoco_QL.setText('--')
        self.SensorOutput_QL.setText('--')

        # Select detection source
        self.yoloFile_QB.clicked.connect(self.open_src_file)  # select local file

        # start testing button
        self.yoloDetect_QB.clicked.connect(self.detect)  # pause/start


    # select local file
    def open_src_file(self):
        config_file = 'config/fold.json'
        config = json.load(open(config_file, 'r', encoding='utf-8'))
        open_fold = config['open_fold']
        if not os.path.exists(open_fold):
            open_fold = os.getcwd()
        name, _ = QFileDialog.getOpenFileName(self, 'Video/image', open_fold,
                                              "Pic File(*.mp4 *.mkv *.avi *.flv *.jpg *.png)")
        if name:
            # self.yolo_predict.source = name
            self.show_status('Load File：{}'.format(os.path.basename(name)))
            config['open_fold'] = os.path.dirname(name)
            config_json = json.dumps(config, ensure_ascii=False, indent=2)
            with open(config_file, 'w', encoding='utf-8') as f:
                f.write(config_json)
            # self.stop()

        # Control start/pause
    def detect(self):
        if self.yolo_predict.source == '':
            self.show_status('Please select a media source before starting detection...')
            self.run_button.setChecked(False)
        else:
            self.yolo_predict.stop_dtc = False
            if self.run_button.isChecked():
                self.run_button.setChecked(True)  # start button
                self.save_txt_button.setEnabled(
                    False)  # It is forbidden to check and save after starting the detection
                self.save_res_button.setEnabled(False)
                self.show_status('Detecting...')
                self.yolo_predict.continue_dtc = True  # Control whether Yolo is paused
                if not self.yolo_thread.isRunning():
                    self.yolo_thread.start()
                    self.main2yolo_begin_sgl.emit()

            else:
                self.yolo_predict.continue_dtc = False
                self.show_status("Pause...")
                self.run_button.setChecked(False)  # start button


    # Cycle monitoring model file changes
    def ModelBoxRefre(self):
        pt_list = os.listdir('./models')
        pt_list = [file for file in pt_list if file.endswith('.pt')]
        pt_list.sort(key=lambda x: os.path.getsize('./models/' + x))
        # It must be sorted before comparing, otherwise the list will be refreshed all the time
        if pt_list != self.pt_list:
            self.pt_list = pt_list
            self.model_box.clear()
            self.model_box.addItems(self.pt_list)


    # bottom status bar information
    def show_status(self, msg):
        self.status_bar.setText(msg)
        # if msg == 'Detection completed':
        #     self.save_res_button.setEnabled(True)
        #     self.save_txt_button.setEnabled(True)
        #     self.run_button.setChecked(False)
        #     self.progress_bar.setValue(0)
        #     if self.yolo_thread.isRunning():
        #         self.yolo_thread.quit()  # end process
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
            # self.yolo_predict.iou_thres = x / 100
        elif flag == 'conf_spinbox':
            self.conf_slider.setValue(int(x * 100))
        elif flag == 'conf_slider':
            self.conf_spinbox.setValue(x / 100)
            self.show_status('Conf Threshold: %s' % str(x / 100))
            # self.yolo_predict.conf_thres = x / 100

        # change model
    def change_model(self, x):
        self.select_model = self.model_box.currentText()
        self.yolo_predict.new_model_name = "./models/%s" % self.select_model
        self.show_status('Change Model：%s' % self.select_model)
        self.Model_name.setText(self.select_model)

    def close(self):
        sys.exit(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Home = MainWindow()
    Home.show()
    sys.exit(app.exec())