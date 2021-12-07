# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Quorra\Python-Projects\Sorting-Algorithms-Visualisation\qt_designer_ozan\main_uiqt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
        MainWindow.setStyleSheet("#MainWindow{\n"
"background-color: rgb(219, 240, 242);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_main_menu = QtWidgets.QFrame(self.centralwidget)
        self.frame_main_menu.setGeometry(QtCore.QRect(0, 0, 1182, 781))
        self.frame_main_menu.setStyleSheet("#MainWindow{\n"
"background-color: rgb(208, 23qlineargradient(spread:reflect, x1:0, y1:0.279, x2:1, y2:0.83, stop:0 rgba(26, 214, 24, 255), stop:1 rgba(68, 184, 255, 255))2, 242);}")
        self.frame_main_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main_menu.setObjectName("frame_main_menu")
        self.layoutWidget = QtWidgets.QWidget(self.frame_main_menu)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 1181, 213))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(491, 211))
        self.pushButton.setMaximumSize(QtCore.QSize(491, 211))
        self.pushButton.setStyleSheet("#pushButton{background-color: rgba(255, 255, 255,0);\n"
"}\n"
"")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/logo_english_university.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(491, 211))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_mail = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_mail.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.pushButton_mail.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/icon_feed_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_mail.setIcon(icon1)
        self.pushButton_mail.setIconSize(QtCore.QSize(55, 55))
        self.pushButton_mail.setObjectName("pushButton_mail")
        self.horizontalLayout_4.addWidget(self.pushButton_mail)
        self.pushButton_information = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_information.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.pushButton_information.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/images/icon_information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_information.setIcon(icon2)
        self.pushButton_information.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_information.setObjectName("pushButton_information")
        self.horizontalLayout_4.addWidget(self.pushButton_information)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_main_menu)
        self.layoutWidget1.setGeometry(QtCore.QRect(1, 225, 1181, 481))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sort_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.sort_button.setMinimumSize(QtCore.QSize(256, 42))
        self.sort_button.setMaximumSize(QtCore.QSize(256, 42))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.sort_button.setFont(font)
        self.sort_button.setStyleSheet("#sort_button{\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0.994, y2:0.768, stop:0 rgba(103, 126, 198, 255), stop:1 rgba(91, 255, 96, 255));\n"
"}\n"
"\n"
"#sort_button:hover{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.279, x2:1, y2:0.83, stop:0 rgba(26, 214, 24, 255), stop:1 rgba(68, 184, 255, 255));}")
        self.sort_button.setObjectName("sort_button")
        self.verticalLayout_2.addWidget(self.sort_button)
        self.timecomp_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.timecomp_button.setMinimumSize(QtCore.QSize(256, 42))
        self.timecomp_button.setMaximumSize(QtCore.QSize(256, 42))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.timecomp_button.setFont(font)
        self.timecomp_button.setStyleSheet("#timecomp_button{\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0.994, y2:0.768, stop:0 rgba(103, 126, 198, 255), stop:1 rgba(91, 255, 96, 255));\n"
"}\n"
"\n"
"#timecomp_button:hover{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.279, x2:1, y2:0.83, stop:0 rgba(26, 214, 24, 255), stop:1 rgba(68, 184, 255, 255));}")
        self.timecomp_button.setObjectName("timecomp_button")
        self.verticalLayout_2.addWidget(self.timecomp_button)
        self.matrix_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.matrix_button.setMinimumSize(QtCore.QSize(256, 42))
        self.matrix_button.setMaximumSize(QtCore.QSize(256, 42))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.matrix_button.setFont(font)
        self.matrix_button.setStyleSheet("#matrix_button{\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0.994, y2:0.768, stop:0 rgba(103, 126, 198, 255), stop:1 rgba(91, 255, 96, 255));\n"
"}\n"
"\n"
"#matrix_button:hover{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.279, x2:1, y2:0.83, stop:0 rgba(26, 214, 24, 255), stop:1 rgba(68, 184, 255, 255));}")
        self.matrix_button.setObjectName("matrix_button")
        self.verticalLayout_2.addWidget(self.matrix_button)
        self.binary_search_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.binary_search_button.setMinimumSize(QtCore.QSize(256, 42))
        self.binary_search_button.setMaximumSize(QtCore.QSize(256, 42))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.binary_search_button.setFont(font)
        self.binary_search_button.setStyleSheet("#binary_search_button{\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0.994, y2:0.768, stop:0 rgba(103, 126, 198, 255), stop:1 rgba(91, 255, 96, 255));\n"
"}\n"
"\n"
"#binary_search_button:hover{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.279, x2:1, y2:0.83, stop:0 rgba(26, 214, 24, 255), stop:1 rgba(68, 184, 255, 255));}")
        self.binary_search_button.setObjectName("binary_search_button")
        self.verticalLayout_2.addWidget(self.binary_search_button)
        self.fibonacci_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.fibonacci_button.setMinimumSize(QtCore.QSize(256, 42))
        self.fibonacci_button.setMaximumSize(QtCore.QSize(256, 42))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fibonacci_button.setFont(font)
        self.fibonacci_button.setStyleSheet("#fibonacci_button{\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0.994, y2:0.768, stop:0 rgba(103, 126, 198, 255), stop:1 rgba(91, 255, 96, 255));\n"
"}\n"
"\n"
"#fibonacci_button:hover{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.279, x2:1, y2:0.83, stop:0 rgba(26, 214, 24, 255), stop:1 rgba(68, 184, 255, 255));}")
        self.fibonacci_button.setObjectName("fibonacci_button")
        self.verticalLayout_2.addWidget(self.fibonacci_button)
        self.kthsmallest_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.kthsmallest_button.setMinimumSize(QtCore.QSize(256, 42))
        self.kthsmallest_button.setMaximumSize(QtCore.QSize(256, 42))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kthsmallest_button.setFont(font)
        self.kthsmallest_button.setStyleSheet("#kthsmallest_button{\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0.994, y2:0.768, stop:0 rgba(103, 126, 198, 255), stop:1 rgba(91, 255, 96, 255));\n"
"}\n"
"\n"
"#kthsmallest_button:hover{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.279, x2:1, y2:0.83, stop:0 rgba(26, 214, 24, 255), stop:1 rgba(68, 184, 255, 255));}")
        self.kthsmallest_button.setObjectName("kthsmallest_button")
        self.verticalLayout_2.addWidget(self.kthsmallest_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame_main_menu)
        self.layoutWidget2.setGeometry(QtCore.QRect(7, 710, 1171, 63))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(564, 61))
        self.pushButton_2.setMaximumSize(QtCore.QSize(564, 61))
        self.pushButton_2.setStyleSheet("#pushButton_2{background-color: rgba(255, 255, 255,0);\n"
"}\n"
"")
        self.pushButton_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/created_by_ozan.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QtCore.QSize(564, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.mic_btn = QtWidgets.QPushButton(self.layoutWidget2)
        self.mic_btn.setStyleSheet("#mic_btn{background-color: rgba(0,0,0,0);}\n"
"\n"
"#mic_btn:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.453136, x2:1, y2:0.523273, stop:0 rgba(104, 113, 138, 255), stop:1 rgba(215, 221, 232, 255));}")
        self.mic_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/images/microphone.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mic_btn.setIcon(icon4)
        self.mic_btn.setIconSize(QtCore.QSize(50, 50))
        self.mic_btn.setObjectName("mic_btn")
        self.horizontalLayout_3.addWidget(self.mic_btn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Visit Izmir Katip Celebi University website.</p></body></html>"))
        self.pushButton_mail.setToolTip(_translate("MainWindow", "Send Feedback"))
        self.pushButton_information.setToolTip(_translate("MainWindow", "Get Information"))
        self.sort_button.setText(_translate("MainWindow", "SORTING ALGORITHMS"))
        self.timecomp_button.setText(_translate("MainWindow", "TIME COMPARISON"))
        self.matrix_button.setText(_translate("MainWindow", "MATRIX MULTIPLICATION"))
        self.binary_search_button.setText(_translate("MainWindow", "BINARY SEARCH"))
        self.fibonacci_button.setText(_translate("MainWindow", "FIBONACCI NUMBER"))
        self.kthsmallest_button.setText(_translate("MainWindow", "RANDOMIZED SELECTION"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
