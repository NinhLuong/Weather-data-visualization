# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainFWqZmd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1259, 1258)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 255, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(97, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 20)
        self.horizontalLayout_3.setStretch(2, 2)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"/*background-color: qconicalgradient(cx:0.5, cy:0.5, angle:224.5, stop:0 rgba(245, 245, 245, 255), stop:0.25 rgba(245, 245, 245, 255), stop:0.251351 rgba(0, 0, 0, 0));\n"
"*/\n"
"border-radius: 150px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:224.5, stop:0 rgba(245, 245, 245, 255), stop:0.99005 rgba(245, 245, 245, 255), stop:1 rgba(0, 0, 0, 0));")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(14, 14, 14, 14)
        self.frame_nhietdo = QFrame(self.frame_9)
        self.frame_nhietdo.setObjectName(u"frame_nhietdo")
        self.frame_nhietdo.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"border-radius: 136px;")
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

        self.frame_chart1 = QFrame(self.frame_2)
        self.frame_chart1.setObjectName(u"frame_chart1")
        self.frame_chart1.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_chart1.setFrameShape(QFrame.StyledPanel)
        self.frame_chart1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_chart1)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.scatter_chart_8 = QVBoxLayout()
        self.scatter_chart_8.setObjectName(u"scatter_chart_8")

        self.verticalLayout_29.addLayout(self.scatter_chart_8)

        self.verticalLayout_29.setStretch(0, 5)

        self.horizontalLayout.addWidget(self.frame_chart1)

        self.frame_do_am = QFrame(self.frame_2)
        self.frame_do_am.setObjectName(u"frame_do_am")
        self.frame_do_am.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:224.5, stop:0 rgba(245, 245, 245, 255), stop:0.25 rgba(245, 245, 245, 255), stop:0.251351 rgba(0, 0, 0, 0));\n"
"border-radius: 150px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:224.5, stop:0 rgba(245, 245, 245, 255), stop:0.99005 rgba(245, 245, 245, 255), stop:1 rgba(0, 0, 0, 0));")
        self.frame_do_am.setFrameShape(QFrame.StyledPanel)
        self.frame_do_am.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_do_am)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(14, 14, 14, 14)
        self.frame_40 = QFrame(self.frame_do_am)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"border-radius: 136px;")
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
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(170, 170, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_chart2 = QFrame(self.frame_3)
        self.frame_chart2.setObjectName(u"frame_chart2")
        self.frame_chart2.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_chart2.setFrameShape(QFrame.StyledPanel)
        self.frame_chart2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_chart2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.line_chart = QVBoxLayout()
        self.line_chart.setObjectName(u"line_chart")

        self.verticalLayout_23.addLayout(self.line_chart)

        self.verticalLayout_23.setStretch(0, 5)

        self.gridLayout_2.addWidget(self.frame_chart2, 0, 0, 1, 1)

        self.frame_chart3 = QFrame(self.frame_3)
        self.frame_chart3.setObjectName(u"frame_chart3")
        self.frame_chart3.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_chart3.setFrameShape(QFrame.StyledPanel)
        self.frame_chart3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_chart3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.scatter_chart = QVBoxLayout()
        self.scatter_chart.setObjectName(u"scatter_chart")

        self.verticalLayout_21.addLayout(self.scatter_chart)

        self.verticalLayout_21.setStretch(0, 5)

        self.gridLayout_2.addWidget(self.frame_chart3, 0, 1, 1, 1)

        self.frame_chart4 = QFrame(self.frame_3)
        self.frame_chart4.setObjectName(u"frame_chart4")
        self.frame_chart4.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_chart4.setFrameShape(QFrame.StyledPanel)
        self.frame_chart4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_chart4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.bar_chart = QVBoxLayout()
        self.bar_chart.setObjectName(u"bar_chart")

        self.verticalLayout_22.addLayout(self.bar_chart)

        self.verticalLayout_22.setStretch(0, 5)

        self.gridLayout_2.addWidget(self.frame_chart4, 1, 0, 1, 1)

        self.frame_chart5 = QFrame(self.frame_3)
        self.frame_chart5.setObjectName(u"frame_chart5")
        self.frame_chart5.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_chart5.setFrameShape(QFrame.StyledPanel)
        self.frame_chart5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_chart5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.histogram_chart = QVBoxLayout()
        self.histogram_chart.setObjectName(u"histogram_chart")

        self.verticalLayout_20.addLayout(self.histogram_chart)


        self.gridLayout_2.addWidget(self.frame_chart5, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 85, 0);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.load_button = QPushButton(self.frame_4)
        self.load_button.setObjectName(u"load_button")
        font2 = QFont()
        font2.setPointSize(10)
        self.load_button.setFont(font2)
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

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.start_button = QPushButton(self.frame_4)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setFont(font2)
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

        self.notice_label = QLabel(self.frame_4)
        self.notice_label.setObjectName(u"notice_label")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setItalic(True)
        self.notice_label.setFont(font3)

        self.horizontalLayout_2.addWidget(self.notice_label)

        self.help_button = QPushButton(self.frame_4)
        self.help_button.setObjectName(u"help_button")
        self.help_button.setFont(font2)
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

        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(4, 1)

        self.verticalLayout.addWidget(self.frame_4)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 10)
        self.verticalLayout.setStretch(3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1259, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Data visualization app", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ninh", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"0\u00b0C", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ed9 \u1ea9m", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input city name", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.notice_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ff0000;\">TextLabel</span></p></body></html>", None))
        self.help_button.setText(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


