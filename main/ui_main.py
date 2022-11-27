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
        MainWindow.resize(1133, 1074)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setIconSize(QSize(50, 50))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
        self.label.setStyleSheet(u"image: url(:/img/main_logo.png);")

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
        self.label_5.setStyleSheet(u"image: url(:/img/Logo_khoa_dien.png);")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 4)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border-radius:20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setEnabled(False)
        self.frame_9.setStyleSheet(u"/*background-color: qconicalgradient(cx:0.5, cy:0.5, angle:224.5, stop:0 rgba(245, 245, 245, 255), stop:0.25 rgba(245, 245, 245, 255), stop:0.251351 rgba(0, 0, 0, 0));\n"
"*/\n"
"border-radius: 100px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:224.5, stop:0 rgba(245, 245, 245, 255), stop:0.99005 rgba(245, 245, 245, 255), stop:1 rgba(0, 0, 0, 0));")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(14, 14, 14, 14)
        self.frame_nhietdo = QFrame(self.frame_9)
        self.frame_nhietdo.setObjectName(u"frame_nhietdo")
        self.frame_nhietdo.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"border-radius: 92px;")
        self.frame_nhietdo.setFrameShape(QFrame.StyledPanel)
        self.frame_nhietdo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_nhietdo)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, 30, -1, -1)
        self.pushButton_33 = QPushButton(self.frame_nhietdo)
        self.pushButton_33.setObjectName(u"pushButton_33")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 201, 0, 255), stop:1 rgba(25, 81, 36, 255));\n"
"background-color: rgba(0, 0, 0, 0);")

        self.verticalLayout_19.addWidget(self.pushButton_33)

        self.pushButton_34 = QPushButton(self.frame_nhietdo)
        self.pushButton_34.setObjectName(u"pushButton_34")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.pushButton_34.setFont(font1)
        self.pushButton_34.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 201, 0, 255), stop:1 rgba(25, 81, 36, 255));\n"
"background-color: rgba(0, 0, 0, 0);")

        self.verticalLayout_19.addWidget(self.pushButton_34)


        self.horizontalLayout_22.addWidget(self.frame_nhietdo)


        self.horizontalLayout.addWidget(self.frame_9)

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame_view = QFrame(self.frame_2)
        self.frame_view.setObjectName(u"frame_view")
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

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_8.addLayout(self.verticalLayout_4)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_8)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.frame_view)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        self.picture = QPushButton(self.frame_view)
        self.picture.setObjectName(u"picture")
        self.picture.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.picture.sizePolicy().hasHeightForWidth())
        self.picture.setSizePolicy(sizePolicy1)
        self.picture.setStyleSheet(u"image: url(:/img/sum.png);")

        self.verticalLayout_5.addWidget(self.picture)

        self.verticalLayout_5.setStretch(1, 3)

        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 1)

        self.horizontalLayout.addWidget(self.frame_view)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.frame_do_am = QFrame(self.frame_2)
        self.frame_do_am.setObjectName(u"frame_do_am")
        self.frame_do_am.setEnabled(False)
        self.frame_do_am.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:224.5, stop:0 rgba(245, 245, 245, 255), stop:0.25 rgba(245, 245, 245, 255), stop:0.251351 rgba(0, 0, 0, 0));\n"
"border-radius: 100px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:224.5, stop:0 rgba(245, 245, 245, 255), stop:0.99005 rgba(245, 245, 245, 255), stop:1 rgba(0, 0, 0, 0));")
        self.frame_do_am.setFrameShape(QFrame.StyledPanel)
        self.frame_do_am.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_do_am)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(14, 14, 14, 14)
        self.frame_40 = QFrame(self.frame_do_am)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"border-radius: 92px;")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_40)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(-1, 30, -1, -1)
        self.pushButton_35 = QPushButton(self.frame_40)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setFont(font)
        self.pushButton_35.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 201, 0, 255), stop:1 rgba(25, 81, 36, 255));\n"
"background-color: rgba(0, 0, 0, 0);")

        self.verticalLayout_81.addWidget(self.pushButton_35)

        self.pushButton_36 = QPushButton(self.frame_40)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setFont(font1)
        self.pushButton_36.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 201, 0, 255), stop:1 rgba(25, 81, 36, 255));\n"
"background-color: rgba(0, 0, 0, 0);")

        self.verticalLayout_81.addWidget(self.pushButton_36)


        self.horizontalLayout_23.addWidget(self.frame_40)


        self.horizontalLayout.addWidget(self.frame_do_am)

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
        self.frame_4.setStyleSheet(u"border-radius:170px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.load_button = QPushButton(self.frame_4)
        self.load_button.setObjectName(u"load_button")
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
        self.lineEdit.setFont(font3)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.start_button = QPushButton(self.frame_4)
        self.start_button.setObjectName(u"start_button")
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

        self.voice = QPushButton(self.frame_4)
        self.voice.setObjectName(u"voice")
        self.voice.setCursor(QCursor(Qt.PointingHandCursor))
        self.voice.setStyleSheet(u"image: url(:/img/mc.png);")

        self.horizontalLayout_2.addWidget(self.voice)

        self.notice_label = QLabel(self.frame_4)
        self.notice_label.setObjectName(u"notice_label")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setItalic(True)
        self.notice_label.setFont(font4)

        self.horizontalLayout_2.addWidget(self.notice_label)

        self.help_button = QPushButton(self.frame_4)
        self.help_button.setObjectName(u"help_button")
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
        self.horizontalLayout_2.setStretch(4, 1)

        self.verticalLayout.addWidget(self.frame_4)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 10)
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Weather Data Visualization", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"L\u01b0\u1ee3ng V\u0169 H\u1ea3i Ninh", None))
        self.label_5.setText("")
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"0\u00b0C", None))
        self.Time.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">7:10</span></p></body></html>", None))
        self.day.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">26/11/2022</span></p></body></html>", None))
        self.thu.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Tuesday</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"  Th\u1eddi ti\u1ebft", None))
        self.picture.setText("")
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ed9 \u1ea9m", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input city name", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.voice.setText("")
        self.notice_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ff0000;\">TextLabel</span></p></body></html>", None))
        self.help_button.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

