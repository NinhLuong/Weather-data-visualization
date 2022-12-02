# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1133, 1121)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1133, 1000))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setIconSize(QSize(30, 30))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1133, 1050))
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));\n"
"background-color: rgb(27, 26, 70);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));\n"
"border-radius:20px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"image: url(:/img/main_logo.png);\n"
"")

        self.horizontalLayout_3.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 15 italic 19pt \"League Spartan\";\n"
"background-color: none;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 15 italic 19pt \"League Spartan\";\n"
"background-color: none;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"image: url(:/img/iconkhoa.png);\n"
"\n"
"")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 4)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgba(42, 44, 111, 255);\n"
"border-radius:20px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.KK_Temp = QFrame(self.frame_2)
        self.KK_Temp.setObjectName(u"KK_Temp")
        self.KK_Temp.setEnabled(True)
        self.KK_Temp.setMinimumSize(QSize(200, 200))
        self.KK_Temp.setMaximumSize(QSize(200, 200))
        self.KK_Temp.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.164179 rgba(255, 255, 0, 255), stop:0.383085 rgba(0, 255, 0, 255), stop:0.402985 rgba(231, 231, 231, 0), stop:0.59204 rgba(255, 255, 255, 0), stop:0.616915 rgba(255, 24, 24, 255), stop:0.905473 rgba(255, 159, 58, 255));\n"
"border-radius: 100px;")
        self.KK_Temp.setFrameShape(QFrame.StyledPanel)
        self.KK_Temp.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.KK_Temp)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.KK_Temp)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(200, 200))
        self.frame_32.setMaximumSize(QSize(200, 200))
        self.frame_32.setStyleSheet(u"background-color: rgba(28, 29, 73, 255);\n"
"border-radius: 100px;")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(14, 14, 14, 14)
        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 0))
        self.frame_33.setMaximumSize(QSize(16777215, 16777215))
        self.frame_33.setStyleSheet(u"background-color:rgba(42, 44, 111, 255);\n"
"border-radius: 86px;")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_33)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(-1, 30, -1, -1)
        self.pushButton_19 = QPushButton(self.frame_33)
        self.pushButton_19.setObjectName(u"pushButton_19")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.verticalLayout_84.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.frame_33)
        self.pushButton_20.setObjectName(u"pushButton_20")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.pushButton_20.setFont(font1)
        self.pushButton_20.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.verticalLayout_84.addWidget(self.pushButton_20)


        self.horizontalLayout_17.addWidget(self.frame_33)


        self.verticalLayout_83.addWidget(self.frame_32)


        self.horizontalLayout.addWidget(self.KK_Temp)

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame_view = QFrame(self.frame_2)
        self.frame_view.setObjectName(u"frame_view")
        self.frame_view.setMinimumSize(QSize(640, 200))
        self.frame_view.setMaximumSize(QSize(640, 200))
        self.frame_view.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_view.setFrameShape(QFrame.StyledPanel)
        self.frame_view.setFrameShadow(QFrame.Raised)
        self.frame_view.setLineWidth(1)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_view)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Time = QLabel(self.frame_view)
        self.Time.setObjectName(u"Time")
        font2 = QFont()
        font2.setFamily(u"Stencil")
        font2.setPointSize(50)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.Time.setFont(font2)
        self.Time.setStyleSheet(u"border: 0px solid black;\n"
"font: 48pt \"Varino Extrude\"rgb(0, 0, 0);\n"
"font: 50pt \"Stencil\"rgb(0, 0, 0);\n"
"")
        self.Time.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.Time)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_3 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.frame_10 = QFrame(self.frame_view)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"border: 0px solid;\n"
"image: url(:/img/agenda.png);\n"
"\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_10)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.day = QLabel(self.frame_view)
        self.day.setObjectName(u"day")
        self.day.setStyleSheet(u"border: 0px solid;\n"
"\n"
"")

        self.verticalLayout_6.addWidget(self.day)

        self.thu = QLabel(self.frame_view)
        self.thu.setObjectName(u"thu")
        self.thu.setStyleSheet(u"border: 0px solid;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")

        self.verticalLayout_6.addWidget(self.thu)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)

        self.horizontalLayout_9.setStretch(0, 2)
        self.horizontalLayout_9.setStretch(1, 2)
        self.horizontalLayout_9.setStretch(2, 5)

        self.verticalLayout_4.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_8.addLayout(self.verticalLayout_4)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_8)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.picture = QPushButton(self.frame_view)
        self.picture.setObjectName(u"picture")
        self.picture.setEnabled(False)
        sizePolicy.setHeightForWidth(self.picture.sizePolicy().hasHeightForWidth())
        self.picture.setSizePolicy(sizePolicy)
        self.picture.setStyleSheet(u"image: url(:/img/sum.png);")

        self.verticalLayout_5.addWidget(self.picture)

        self.verticalLayout_5.setStretch(0, 3)

        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 2)

        self.horizontalLayout.addWidget(self.frame_view)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.KK_Humi = QFrame(self.frame_2)
        self.KK_Humi.setObjectName(u"KK_Humi")
        self.KK_Humi.setEnabled(False)
        self.KK_Humi.setMinimumSize(QSize(200, 200))
        self.KK_Humi.setMaximumSize(QSize(200, 200))
        self.KK_Humi.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:270.7, stop:0.189055 rgba(85, 0, 127, 255), stop:0.343284 rgba(0, 0, 255, 255), stop:0.502488 rgba(0, 170, 0, 255), stop:0.661692 rgba(255, 255, 0, 255), stop:0.80597 rgba(255, 0, 0, 255));\n"
"border-radius: 100px;")
        self.KK_Humi.setFrameShape(QFrame.StyledPanel)
        self.KK_Humi.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.KK_Humi)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.KK_Humi)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setEnabled(False)
        self.frame_34.setMinimumSize(QSize(200, 200))
        self.frame_34.setMaximumSize(QSize(200, 200))
        self.frame_34.setStyleSheet(u"background-color: rgba(28, 29, 73, 255);\n"
"border-radius: 100px;")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(14, 14, 14, 14)
        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 0))
        self.frame_35.setMaximumSize(QSize(16777215, 16777215))
        self.frame_35.setStyleSheet(u"background-color:rgba(42, 44, 111, 255);\n"
"border-radius: 86px;")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_35)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(-1, 30, -1, -1)
        self.pushButton_21 = QPushButton(self.frame_35)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.verticalLayout_86.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.frame_35)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setFont(font1)
        self.pushButton_22.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.verticalLayout_86.addWidget(self.pushButton_22)


        self.horizontalLayout_18.addWidget(self.frame_35)


        self.verticalLayout_85.addWidget(self.frame_34)


        self.horizontalLayout.addWidget(self.KK_Humi)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 3)
        self.horizontalLayout.setStretch(4, 1)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_chart1 = QFrame(self.frame_3)
        self.frame_chart1.setObjectName(u"frame_chart1")
        self.frame_chart1.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgb(255, 255, 255);\n"
"\n"
"")
        self.frame_chart1.setFrameShape(QFrame.StyledPanel)
        self.frame_chart1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_chart1)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.line_chart = QVBoxLayout()
        self.line_chart.setObjectName(u"line_chart")

        self.verticalLayout_23.addLayout(self.line_chart)

        self.verticalLayout_23.setStretch(0, 5)

        self.gridLayout_2.addWidget(self.frame_chart1, 0, 0, 1, 1)

        self.frame_chart2 = QFrame(self.frame_3)
        self.frame_chart2.setObjectName(u"frame_chart2")
        self.frame_chart2.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_chart2.setFrameShape(QFrame.StyledPanel)
        self.frame_chart2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_chart2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.scatter_chart = QVBoxLayout()
        self.scatter_chart.setObjectName(u"scatter_chart")

        self.verticalLayout_21.addLayout(self.scatter_chart)


        self.gridLayout_2.addWidget(self.frame_chart2, 0, 1, 1, 1)

        self.frame_chart3 = QFrame(self.frame_3)
        self.frame_chart3.setObjectName(u"frame_chart3")
        self.frame_chart3.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_chart3.setFrameShape(QFrame.StyledPanel)
        self.frame_chart3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_chart3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.bar_chart = QVBoxLayout()
        self.bar_chart.setObjectName(u"bar_chart")

        self.verticalLayout_22.addLayout(self.bar_chart)

        self.verticalLayout_22.setStretch(0, 5)

        self.gridLayout_2.addWidget(self.frame_chart3, 1, 0, 1, 1)

        self.frame_chart4 = QFrame(self.frame_3)
        self.frame_chart4.setObjectName(u"frame_chart4")
        self.frame_chart4.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_chart4.setFrameShape(QFrame.StyledPanel)
        self.frame_chart4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_chart4)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.histogram_chart = QVBoxLayout()
        self.histogram_chart.setObjectName(u"histogram_chart")

        self.verticalLayout_20.addLayout(self.histogram_chart)


        self.gridLayout_2.addWidget(self.frame_chart4, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border-bottom-right-radius: 0px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));\n"
"border-radius:20px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.load_button = QPushButton(self.frame_4)
        self.load_button.setObjectName(u"load_button")
        self.load_button.setMinimumSize(QSize(81, 31))
        font3 = QFont()
        font3.setPointSize(10)
        self.load_button.setFont(font3)
        self.load_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.load_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(154, 153, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color:rgb(255, 255, 255);\n"
"}\n"
"	")

        self.horizontalLayout_2.addWidget(self.load_button)

        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(81, 31))
        self.lineEdit.setFont(font3)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.start_button = QPushButton(self.frame_4)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(81, 31))
        self.start_button.setFont(font3)
        self.start_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(154, 153, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color:rgb(255, 255, 255);\n"
"}\n"
"	")

        self.horizontalLayout_2.addWidget(self.start_button)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.voice = QPushButton(self.frame_4)
        self.voice.setObjectName(u"voice")
        self.voice.setMinimumSize(QSize(81, 31))
        self.voice.setCursor(QCursor(Qt.PointingHandCursor))
        self.voice.setStyleSheet(u"QPushButton{	\n"
"	image: url(:/img/voice_icon.png);\n"
"	border-radius: 15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.voice)

        self.notice_label = QLabel(self.frame_4)
        self.notice_label.setObjectName(u"notice_label")
        self.notice_label.setMinimumSize(QSize(81, 31))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setItalic(True)
        self.notice_label.setFont(font4)

        self.horizontalLayout_2.addWidget(self.notice_label)

        self.help_button = QPushButton(self.frame_4)
        self.help_button.setObjectName(u"help_button")
        self.help_button.setMinimumSize(QSize(81, 31))
        self.help_button.setFont(font3)
        self.help_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.help_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(154, 153, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color:rgb(255, 255, 255);\n"
"}\n"
"	")

        self.horizontalLayout_2.addWidget(self.help_button)

        self.exit_button = QPushButton(self.frame_4)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMinimumSize(QSize(81, 31))
        self.exit_button.setFont(font3)
        self.exit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.exit_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(154, 153, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(237, 51, 59);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"	")

        self.horizontalLayout_2.addWidget(self.exit_button)

        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(5, 1)

        self.verticalLayout.addWidget(self.frame_4)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 12)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1133, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; font-style:normal;\">Weather Data Visualization</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">L\u01b0\u1ee3ng V\u0169 H\u1ea3i Ninh - 20139083</span></p></body></html>", None))
        self.label_5.setText("")
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"0\u00b0C", None))
        self.Time.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">7:10</span></p></body></html>", None))
        self.day.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">26/11/2022</span></p></body></html>", None))
        self.thu.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Tuesday</span></p></body></html>", None))
        self.picture.setText("")
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ed9 \u1ea9m", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input city name", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.voice.setText("")
        self.notice_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ff0000;\">TextLabel</span></p></body></html>", None))
        self.help_button.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

