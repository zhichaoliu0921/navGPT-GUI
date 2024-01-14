# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)
import ui.resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1763, 1052)
        MainWindow.setMaximumSize(QSize(1920, 16777215))
        self.Main_QW = QWidget(MainWindow)
        self.Main_QW.setObjectName(u"Main_QW")
        self.Main_QW.setMinimumSize(QSize(0, 0))
        self.Main_QW.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.Main_QW)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Main_QF = QFrame(self.Main_QW)
        self.Main_QF.setObjectName(u"Main_QF")
        self.Main_QF.setMaximumSize(QSize(16777215, 16777215))
        self.Main_QF.setStyleSheet(u"QFrame#Main_QF{\n"
"	background-color: rgb(245, 249, 254);\n"
"border:0px solid red;\n"
"border-radius:30px\n"
"}")
        self.Main_QF.setFrameShape(QFrame.StyledPanel)
        self.Main_QF.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Main_QF)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetNoConstraint)
        self.Top = QFrame(self.Main_QF)
        self.Top.setObjectName(u"Top")
        self.Top.setMaximumSize(QSize(16777215, 16777215))
        self.Top.setStyleSheet(u"")
        self.Top.setFrameShape(QFrame.StyledPanel)
        self.Top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.Top)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.Top)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 italic 14pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_9 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_9)

        self.buttons_qf = QFrame(self.Top)
        self.buttons_qf.setObjectName(u"buttons_qf")
        self.buttons_qf.setFrameShape(QFrame.StyledPanel)
        self.buttons_qf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.buttons_qf)
        self.horizontalLayout_13.setSpacing(2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.min_sf = QPushButton(self.buttons_qf)
        self.min_sf.setObjectName(u"min_sf")
        self.min_sf.setMinimumSize(QSize(14, 14))
        self.min_sf.setMaximumSize(QSize(14, 14))
        self.min_sf.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(4, 180, 0);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(232, 59, 35);\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.min_sf)

        self.max_sf = QPushButton(self.buttons_qf)
        self.max_sf.setObjectName(u"max_sf")
        self.max_sf.setMaximumSize(QSize(15, 15))
        self.max_sf.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(227, 199, 0);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(232, 59, 35);\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.max_sf)

        self.close_sf = QPushButton(self.buttons_qf)
        self.close_sf.setObjectName(u"close_sf")
        self.close_sf.setMinimumSize(QSize(15, 15))
        self.close_sf.setMaximumSize(QSize(15, 15))
        self.close_sf.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(240, 108, 96);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(232, 59, 35);\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.close_sf)


        self.verticalLayout_4.addWidget(self.buttons_qf)

        self.verticalSpacer_10 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_10)


        self.horizontalLayout_12.addLayout(self.verticalLayout_4)

        self.horizontalLayout_12.setStretch(0, 20)
        self.horizontalLayout_12.setStretch(1, 1)

        self.verticalLayout_3.addWidget(self.Top)

        self.Bottom = QFrame(self.Main_QF)
        self.Bottom.setObjectName(u"Bottom")
        self.Bottom.setStyleSheet(u"")
        self.Bottom.setFrameShape(QFrame.StyledPanel)
        self.Bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Bottom)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.Left_QF = QFrame(self.Bottom)
        self.Left_QF.setObjectName(u"Left_QF")
        self.Left_QF.setStyleSheet(u"\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px\n"
"")
        self.Left_QF.setFrameShape(QFrame.StyledPanel)
        self.Left_QF.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Left_QF)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.yolo_top = QFrame(self.Left_QF)
        self.yolo_top.setObjectName(u"yolo_top")
        self.yolo_top.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.yolo_top.setFrameShape(QFrame.StyledPanel)
        self.yolo_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.yolo_top)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.yoloOutput_QF = QFrame(self.yolo_top)
        self.yoloOutput_QF.setObjectName(u"yoloOutput_QF")
        self.yoloOutput_QF.setStyleSheet(u"QFrame#yoloOutput_QF{\n"
"background-color: rgb(238, 242, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px;}")
        self.yoloOutput_QF.setFrameShape(QFrame.StyledPanel)
        self.yoloOutput_QF.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.yoloOutput_QF)
        self.verticalLayout_12.setSpacing(1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.yoloOutput_QF)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setStyleSheet(u"padding-left:12px;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_5)

        self.yoloOutput_QF2 = QFrame(self.yoloOutput_QF)
        self.yoloOutput_QF2.setObjectName(u"yoloOutput_QF2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yoloOutput_QF2.sizePolicy().hasHeightForWidth())
        self.yoloOutput_QF2.setSizePolicy(sizePolicy)
        self.yoloOutput_QF2.setFrameShape(QFrame.StyledPanel)
        self.yoloOutput_QF2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.yoloOutput_QF2)
        self.horizontalLayout_6.setSpacing(18)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.yoloModelOutput_QF = QFrame(self.yoloOutput_QF2)
        self.yoloModelOutput_QF.setObjectName(u"yoloModelOutput_QF")
        self.yoloModelOutput_QF.setStyleSheet(u"QFrame#yoloModelOutput_QF{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(162, 129, 247),  stop:1 rgb(119, 111, 252));\n"
"border: 1px outset rgb(98, 91, 213);}")
        self.yoloModelOutput_QF.setFrameShape(QFrame.StyledPanel)
        self.yoloModelOutput_QF.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.yoloModelOutput_QF)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_6 = QLabel(self.yoloModelOutput_QF)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"font: 700 italic 16pt \"Segoe UI\";\n"
"border: 1px solid white;\n"
"border-radius: 0px;\n"
"border-left: none;\n"
"border-top: none;\n"
"border-right: none;\n"
"border-bottom-left-radius: {margin}px 0;\n"
"border-bottom-right-radius: {margin}px 0;\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_6)

        self.modelOutput_QL = QLabel(self.yoloModelOutput_QF)
        self.modelOutput_QL.setObjectName(u"modelOutput_QL")
        self.modelOutput_QL.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 17pt \"Microsoft YaHei UI\";")
        self.modelOutput_QL.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.modelOutput_QL)

        self.verticalLayout_13.setStretch(0, 1)
        self.verticalLayout_13.setStretch(1, 2)

        self.horizontalLayout_7.addLayout(self.verticalLayout_13)


        self.horizontalLayout_6.addWidget(self.yoloModelOutput_QF)

        self.yoloRobotOutput_QF = QFrame(self.yoloOutput_QF2)
        self.yoloRobotOutput_QF.setObjectName(u"yoloRobotOutput_QF")
        self.yoloRobotOutput_QF.setStyleSheet(u"QFrame#yoloRobotOutput_QF{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(162, 129, 247),  stop:1 rgb(119, 111, 252));\n"
"border: 1px outset rgb(98, 91, 213);}")
        self.yoloRobotOutput_QF.setFrameShape(QFrame.StyledPanel)
        self.yoloRobotOutput_QF.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.yoloRobotOutput_QF)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_8 = QLabel(self.yoloRobotOutput_QF)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"font: 700 italic 16pt \"Segoe UI\";\n"
"border: 1px solid white;\n"
"border-radius: 0px;\n"
"border-left: none;\n"
"border-top: none;\n"
"border-right: none;\n"
"border-bottom-left-radius: {margin}px 0;\n"
"border-bottom-right-radius: {margin}px 0;\n"
"")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_8)

        self.RobotOutput_QL = QLabel(self.yoloRobotOutput_QF)
        self.RobotOutput_QL.setObjectName(u"RobotOutput_QL")
        self.RobotOutput_QL.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 17pt \"Microsoft YaHei UI\";")
        self.RobotOutput_QL.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.RobotOutput_QL)

        self.verticalLayout_14.setStretch(0, 1)
        self.verticalLayout_14.setStretch(1, 2)

        self.horizontalLayout_8.addLayout(self.verticalLayout_14)


        self.horizontalLayout_6.addWidget(self.yoloRobotOutput_QF)

        self.yoloLocoOutput_QF = QFrame(self.yoloOutput_QF2)
        self.yoloLocoOutput_QF.setObjectName(u"yoloLocoOutput_QF")
        self.yoloLocoOutput_QF.setStyleSheet(u"QFrame#yoloLocoOutput_QF{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(162, 129, 247),  stop:1 rgb(119, 111, 252));\n"
"border: 1px outset rgb(98, 91, 213);}")
        self.yoloLocoOutput_QF.setFrameShape(QFrame.StyledPanel)
        self.yoloLocoOutput_QF.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.yoloLocoOutput_QF)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_7 = QLabel(self.yoloLocoOutput_QF)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"font: 700 italic 16pt \"Segoe UI\";\n"
"border: 1px solid white;\n"
"border-radius: 0px;\n"
"border-left: none;\n"
"border-top: none;\n"
"border-right: none;\n"
"border-bottom-left-radius: {margin}px 0;\n"
"border-bottom-right-radius: {margin}px 0;\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_7)

        self.modelLoco_TE = QTextEdit(self.yoloLocoOutput_QF)
        self.modelLoco_TE.setObjectName(u"modelLoco_TE")
        sizePolicy.setHeightForWidth(self.modelLoco_TE.sizePolicy().hasHeightForWidth())
        self.modelLoco_TE.setSizePolicy(sizePolicy)
        self.modelLoco_TE.setMaximumSize(QSize(188, 95))
        self.modelLoco_TE.setStyleSheet(u"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(162, 129, 247),  stop:1 rgb(119, 111, 252));\n"
"color: rgb(255, 255, 255);\n"
"font: 17pt \"Microsoft YaHei UI\";\n"
"\n"
"")

        self.verticalLayout_15.addWidget(self.modelLoco_TE)

        self.verticalLayout_15.setStretch(0, 1)
        self.verticalLayout_15.setStretch(1, 2)

        self.horizontalLayout_9.addLayout(self.verticalLayout_15)


        self.horizontalLayout_6.addWidget(self.yoloLocoOutput_QF)

        self.yoloSensorOutput_QF = QFrame(self.yoloOutput_QF2)
        self.yoloSensorOutput_QF.setObjectName(u"yoloSensorOutput_QF")
        self.yoloSensorOutput_QF.setStyleSheet(u"QFrame#yoloSensorOutput_QF{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(162, 129, 247),  stop:1 rgb(119, 111, 252));\n"
"border: 1px outset rgb(98, 91, 213);}")
        self.yoloSensorOutput_QF.setFrameShape(QFrame.StyledPanel)
        self.yoloSensorOutput_QF.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.yoloSensorOutput_QF)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_9 = QLabel(self.yoloSensorOutput_QF)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"font: 700 italic 16pt \"Segoe UI\";\n"
"border: 1px solid white;\n"
"border-radius: 0px;\n"
"border-left: none;\n"
"border-top: none;\n"
"border-right: none;\n"
"border-bottom-left-radius: {margin}px 0;\n"
"border-bottom-right-radius: {margin}px 0;\n"
"")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_9)

        self.SensorOutput_TE = QTextEdit(self.yoloSensorOutput_QF)
        self.SensorOutput_TE.setObjectName(u"SensorOutput_TE")
        sizePolicy.setHeightForWidth(self.SensorOutput_TE.sizePolicy().hasHeightForWidth())
        self.SensorOutput_TE.setSizePolicy(sizePolicy)
        self.SensorOutput_TE.setMaximumSize(QSize(188, 95))
        self.SensorOutput_TE.setStyleSheet(u"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(162, 129, 247),  stop:1 rgb(119, 111, 252));\n"
"color: rgb(255, 255, 255);\n"
"font: 17pt \"Microsoft YaHei UI\";\n"
"")

        self.verticalLayout_16.addWidget(self.SensorOutput_TE)

        self.verticalLayout_16.setStretch(0, 1)
        self.verticalLayout_16.setStretch(1, 2)

        self.horizontalLayout_10.addLayout(self.verticalLayout_16)


        self.horizontalLayout_6.addWidget(self.yoloSensorOutput_QF)


        self.verticalLayout_12.addWidget(self.yoloOutput_QF2)

        self.verticalLayout_12.setStretch(0, 1)
        self.verticalLayout_12.setStretch(1, 25)

        self.verticalLayout_11.addWidget(self.yoloOutput_QF)

        self.yoloVisual_QF = QFrame(self.yolo_top)
        self.yoloVisual_QF.setObjectName(u"yoloVisual_QF")
        self.yoloVisual_QF.setStyleSheet(u"QFrame#yoloVisual_QF{\n"
"background-color: rgb(238, 242, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px;}")
        self.yoloVisual_QF.setFrameShape(QFrame.StyledPanel)
        self.yoloVisual_QF.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.yoloVisual_QF)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.status_bar = QLabel(self.yoloVisual_QF)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setStyleSheet(u"font: 700 11pt \"Segoe UI\";\n"
"color: rgba(0, 0, 0, 140);\n"
"padding-left:15px;")

        self.verticalLayout_17.addWidget(self.status_bar)

        self.label_10 = QLabel(self.yoloVisual_QF)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background-color: rgb(238, 242, 255);\n"
"border:0px solid rgb(255, 255, 255);\n"
"border-radius:15px")

        self.verticalLayout_17.addWidget(self.label_10)

        self.progressBar = QProgressBar(self.yoloVisual_QF)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy1)
        self.progressBar.setMinimumSize(QSize(0, 20))
        self.progressBar.setMaximumSize(QSize(16777215, 20))
        self.progressBar.setStyleSheet(u"QProgressBar{ \n"
"font: 700 10pt \"Microsoft YaHei UI\";\n"
"color: rgb(253, 143, 134); \n"
"text-align:center; \n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"background-color: rgba(215, 215, 215,100);\n"
"} \n"
"\n"
"QProgressBar:chunk{ \n"
"border-radius:0px; \n"
"background: rgba(119, 111, 252, 200);\n"
"border-radius: 7px;\n"
"}")
        self.progressBar.setValue(0)

        self.verticalLayout_17.addWidget(self.progressBar)

        self.verticalLayout_17.setStretch(0, 1)
        self.verticalLayout_17.setStretch(1, 25)
        self.verticalLayout_17.setStretch(2, 1)

        self.horizontalLayout_11.addLayout(self.verticalLayout_17)


        self.verticalLayout_11.addWidget(self.yoloVisual_QF)

        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 3)

        self.horizontalLayout_5.addLayout(self.verticalLayout_11)


        self.verticalLayout_5.addWidget(self.yolo_top)

        self.yolo_down = QFrame(self.Left_QF)
        self.yolo_down.setObjectName(u"yolo_down")
        self.yolo_down.setStyleSheet(u"QFrame#yolo_down{background-color: qlineargradient(spread:pad, x1:0.483, y1:1, x2:0.472, y2:0.0227273, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border:0px solid red;\n"
"border-radius:30px\n"
"}\n"
"")
        self.yolo_down.setFrameShape(QFrame.StyledPanel)
        self.yolo_down.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.yolo_down)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.yoloSave_QB = QPushButton(self.yolo_down)
        self.yoloSave_QB.setObjectName(u"yoloSave_QB")
        self.yoloSave_QB.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/save.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(0, 0, 0, 199);\n"
"font: 700 14pt \"Nirmala UI\";\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")

        self.gridLayout.addWidget(self.yoloSave_QB, 2, 3, 1, 1)

        self.yoloFile_QB = QPushButton(self.yolo_down)
        self.yoloFile_QB.setObjectName(u"yoloFile_QB")
        self.yoloFile_QB.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/media.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border:none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(0, 0, 0, 199);\n"
"font: 700 14pt \"Nirmala UI\";\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")

        self.gridLayout.addWidget(self.yoloFile_QB, 2, 0, 1, 1)

        self.yoloDetect_QB = QPushButton(self.yolo_down)
        self.yoloDetect_QB.setObjectName(u"yoloDetect_QB")
        self.yoloDetect_QB.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/start.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(0, 0, 0, 199);\n"
"font: 700 14pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")

        self.gridLayout.addWidget(self.yoloDetect_QB, 2, 2, 1, 1)

        self.yoloSaveLabel_QB = QPushButton(self.yolo_down)
        self.yoloSaveLabel_QB.setObjectName(u"yoloSaveLabel_QB")
        self.yoloSaveLabel_QB.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/save_txt.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(0, 0, 0, 199);\n"
"font: 700 14pt \"Nirmala UI\";\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")

        self.gridLayout.addWidget(self.yoloSaveLabel_QB, 2, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.yoloIOUframe = QFrame(self.yolo_down)
        self.yoloIOUframe.setObjectName(u"yoloIOUframe")
        self.yoloIOUframe.setStyleSheet(u"QFrame#yoloIOUframe{\n"
"border:1px solid white;\n"
"border-radius:30px\n"
"}")
        self.yoloIOUframe.setFrameShape(QFrame.StyledPanel)
        self.yoloIOUframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.yoloIOUframe)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.pushButton = QPushButton(self.yoloIOUframe)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/IOU2.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(0, 0, 0, 199);\n"
"font: 700 14pt \"Nirmala UI\";\n"
"}")

        self.verticalLayout_8.addWidget(self.pushButton)

        self.yoloIOUframe_2 = QFrame(self.yoloIOUframe)
        self.yoloIOUframe_2.setObjectName(u"yoloIOUframe_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.yoloIOUframe_2.sizePolicy().hasHeightForWidth())
        self.yoloIOUframe_2.setSizePolicy(sizePolicy2)
        self.yoloIOUframe_2.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.yoloIOUframe_2.setFrameShape(QFrame.StyledPanel)
        self.yoloIOUframe_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.yoloIOUframe_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.iou_slider = QSlider(self.yoloIOUframe_2)
        self.iou_slider.setObjectName(u"iou_slider")
        self.iou_slider.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(15)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.iou_slider.sizePolicy().hasHeightForWidth())
        self.iou_slider.setSizePolicy(sizePolicy3)
        self.iou_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: none;\n"
"height: 10px;\n"
"background-color: rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 10px;\n"
"margin: -1px 0px -1px 0px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"border-radius: 5px;\n"
"}")
        self.iou_slider.setMaximum(100)
        self.iou_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_9.addWidget(self.iou_slider)

        self.verticalSpacer_8 = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_8)

        self.iou_spinbox = QDoubleSpinBox(self.yoloIOUframe_2)
        self.iou_spinbox.setObjectName(u"iou_spinbox")
        self.iou_spinbox.setStyleSheet(u"QDoubleSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color: rgba(255,255,255,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"}\n"
"        \n"
"QDoubleSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QDoubleSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")

        self.verticalLayout_9.addWidget(self.iou_spinbox)


        self.verticalLayout_8.addWidget(self.yoloIOUframe_2)


        self.gridLayout.addWidget(self.yoloIOUframe, 0, 3, 1, 1)

        self.yoloModelframe = QFrame(self.yolo_down)
        self.yoloModelframe.setObjectName(u"yoloModelframe")
        self.yoloModelframe.setStyleSheet(u"QFrame#yoloModelframe{\n"
"border:1px solid white;\n"
"border-radius:30px\n"
"}")
        self.yoloModelframe.setFrameShape(QFrame.StyledPanel)
        self.yoloModelframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.yoloModelframe)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.yoloModelButton = QPushButton(self.yoloModelframe)
        self.yoloModelButton.setObjectName(u"yoloModelButton")
        self.yoloModelButton.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/yolo.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(0, 0, 0, 199);\n"
"font: 700 14pt \"Nirmala UI\";\n"
"}")

        self.verticalLayout_6.addWidget(self.yoloModelButton)

        self.yoloModel_CB = QComboBox(self.yoloModelframe)
        self.yoloModel_CB.setObjectName(u"yoloModel_CB")
        self.yoloModel_CB.setStyleSheet(u"QComboBox {\n"
"            background-color: rgba(255,255,255,90);\n"
"			color: rgba(0, 0, 0, 200);\n"
"			font: 600 9pt \"Segoe UI\";\n"
"            border: 1px solid lightgray;\n"
"            border-radius: 10px;\n"
"            padding-left: 20px;\n"
"        }\n"
"        \n"
"        QComboBox:on {\n"
"            border: 1px solid #63acfb;\n"
"        }\n"
"\n"
"        QComboBox::drop-down {\n"
"            width: 22px;\n"
"            border-left: 1px solid lightgray;\n"
"            border-top-right-radius: 15px;\n"
"            border-bottom-right-radius: 15px;\n"
"        }\n"
"        \n"
"        QComboBox::drop-down:on {\n"
"            border-left: 1px solid #63acfb;\n"
"        }\n"
"\n"
"        QComboBox::down-arrow {\n"
"            width: 16px;\n"
"            height: 16px;\n"
"            image: url(:/all/img/box_down.png);\n"
"        }\n"
"\n"
"        QComboBox::down-arrow:on {\n"
"            image: url(:/all/img/box_up.png);\n"
"        }\n"
"\n"
"        QComboBox QAbstractItemVi"
                        "ew {\n"
"            border: none;\n"
"            outline: none;\n"
"			padding: 10px;\n"
"            background-color: rgb(223, 188, 220);\n"
"        }\n"
"\n"
"\n"
"        QComboBox QScrollBar:vertical {\n"
"            width: 2px;\n"
"           background-color: rgba(255,255,255,150);\n"
"        }\n"
"\n"
"        QComboBox QScrollBar::handle:vertical {\n"
"            background-color: rgba(255,255,255,90);\n"
"        }")

        self.verticalLayout_6.addWidget(self.yoloModel_CB)


        self.gridLayout.addWidget(self.yoloModelframe, 0, 2, 1, 1)

        self.nameframe = QFrame(self.yolo_down)
        self.nameframe.setObjectName(u"nameframe")
        self.nameframe.setStyleSheet(u"QFrame#nameframe{\n"
"border:1px solid white;\n"
"border-radius:30px\n"
"}")
        self.nameframe.setFrameShape(QFrame.StyledPanel)
        self.nameframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.nameframe)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.namewidget = QWidget(self.nameframe)
        self.namewidget.setObjectName(u"namewidget")
        self.namewidget.setStyleSheet(u"QWidget{\n"
"border:none;\n"
"image: url(:/all/img/logo.png);\n"
"border-radius:10px\n"
"}")

        self.horizontalLayout_3.addWidget(self.namewidget)

        self.nameframe_2 = QFrame(self.nameframe)
        self.nameframe_2.setObjectName(u"nameframe_2")
        self.nameframe_2.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.nameframe_2.setFrameShape(QFrame.StyledPanel)
        self.nameframe_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.nameframe_2)
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)

        self.label_2 = QLabel(self.nameframe_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(0, 0, 0, 199);\n"
"font: 700 18pt \"Nirmala UI\";")

        self.verticalLayout_10.addWidget(self.label_2)

        self.label_3 = QLabel(self.nameframe_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(0, 0, 0, 199);\n"
"font: 700 12pt \"Nirmala UI\";")

        self.verticalLayout_10.addWidget(self.label_3)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_6)

        self.label_4 = QLabel(self.nameframe_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(0, 0, 0, 199);\n"
"font: 700 12pt \"Nirmala UI\";")

        self.verticalLayout_10.addWidget(self.label_4)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)


        self.horizontalLayout_3.addWidget(self.nameframe_2)


        self.gridLayout.addWidget(self.nameframe, 0, 0, 1, 1)

        self.yoloConfframe = QFrame(self.yolo_down)
        self.yoloConfframe.setObjectName(u"yoloConfframe")
        self.yoloConfframe.setStyleSheet(u"QFrame#yoloConfframe{\n"
"border:1px solid white;\n"
"border-radius:30px\n"
"}")
        self.yoloConfframe.setFrameShape(QFrame.StyledPanel)
        self.yoloConfframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.yoloConfframe)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)

        self.pushButton_2 = QPushButton(self.yoloConfframe)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/setting.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(0, 0, 0, 199);\n"
"font: 700 14pt \"Nirmala UI\";\n"
"}")

        self.verticalLayout_7.addWidget(self.pushButton_2)

        self.conf_slider = QSlider(self.yoloConfframe)
        self.conf_slider.setObjectName(u"conf_slider")
        sizePolicy3.setHeightForWidth(self.conf_slider.sizePolicy().hasHeightForWidth())
        self.conf_slider.setSizePolicy(sizePolicy3)
        self.conf_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: none;\n"
"height: 10px;\n"
"background-color: rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 10px;\n"
"margin: -1px 0px -1px 0px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"border-radius: 5px;\n"
"}")
        self.conf_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_7.addWidget(self.conf_slider)

        self.conf_spinbox = QDoubleSpinBox(self.yoloConfframe)
        self.conf_spinbox.setObjectName(u"conf_spinbox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.conf_spinbox.sizePolicy().hasHeightForWidth())
        self.conf_spinbox.setSizePolicy(sizePolicy4)
        self.conf_spinbox.setStyleSheet(u"QDoubleSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color: rgba(255,255,255,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"}\n"
"        \n"
"QDoubleSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QDoubleSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")

        self.verticalLayout_7.addWidget(self.conf_spinbox)


        self.gridLayout.addWidget(self.yoloConfframe, 0, 4, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout_5.addWidget(self.yolo_down)

        self.verticalLayout_5.setStretch(0, 4)
        self.verticalLayout_5.setStretch(1, 1)

        self.verticalLayout.addLayout(self.verticalLayout_5)


        self.horizontalLayout_4.addWidget(self.Left_QF)

        self.Right_QF = QFrame(self.Bottom)
        self.Right_QF.setObjectName(u"Right_QF")
        self.Right_QF.setStyleSheet(u"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px")
        self.Right_QF.setFrameShape(QFrame.StyledPanel)
        self.Right_QF.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.Right_QF)


        self.verticalLayout_3.addWidget(self.Bottom)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 30)

        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addWidget(self.Main_QF)

        MainWindow.setCentralWidget(self.Main_QW)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"NavGPT Ver 1.0 by ZL", None))
        self.min_sf.setText("")
        self.max_sf.setText("")
        self.close_sf.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Detection", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Use Model", None))
        self.modelOutput_QL.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Robot", None))
        self.RobotOutput_QL.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Locomotion", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Perception", None))
        self.status_bar.setText(QCoreApplication.translate("MainWindow", u"Welcome!", None))
        self.label_10.setText("")
        self.yoloSave_QB.setText(QCoreApplication.translate("MainWindow", u"Save File", None))
        self.yoloFile_QB.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.yoloDetect_QB.setText(QCoreApplication.translate("MainWindow", u"Detect", None))
        self.yoloSaveLabel_QB.setText(QCoreApplication.translate("MainWindow", u"Save Label", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"IOU", None))
        self.yoloModelButton.setText(QCoreApplication.translate("MainWindow", u"Select Model", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"NavGPT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version 1.0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"By Zhichao", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Confidence", None))
    # retranslateUi

