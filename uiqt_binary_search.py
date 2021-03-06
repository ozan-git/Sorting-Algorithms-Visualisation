# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Quorra\Python-Projects\Sorting-Algorithms-Visualisation\qt_designer_ozan\binary_search_uiqt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BinarySearchWindow(object):
    def setupUi(self, BinarySearchWindow):
        BinarySearchWindow.setObjectName("BinarySearchWindow")
        BinarySearchWindow.resize(1200, 903)
        BinarySearchWindow.setMinimumSize(QtCore.QSize(1200, 880))
        BinarySearchWindow.setMaximumSize(QtCore.QSize(4500, 4500))
        BinarySearchWindow.setStyleSheet("#BinarySearchWindow{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.193545, x2:1, y2:0.676, stop:0 rgba(30, 187, 114, 255), stop:1 rgba(122, 89, 196, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(BinarySearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_main_binary = QtWidgets.QVBoxLayout()
        self.frame_main_binary.setSpacing(0)
        self.frame_main_binary.setObjectName("frame_main_binary")
        self.frame_top_binary = QtWidgets.QFrame(self.centralwidget)
        self.frame_top_binary.setMinimumSize(QtCore.QSize(1180, 0))
        self.frame_top_binary.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_top_binary.setStyleSheet("background-color: transparent;")
        self.frame_top_binary.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_binary.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_binary.setObjectName("frame_top_binary")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_top_binary)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.frame_top_right_3 = QtWidgets.QFrame(self.frame_top_binary)
        self.frame_top_right_3.setStyleSheet("background: transparent;")
        self.frame_top_right_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_right_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_right_3.setObjectName("frame_top_right_3")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_top_right_3)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_top_btns_3 = QtWidgets.QFrame(self.frame_top_right_3)
        self.frame_top_btns_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_top_btns_3.setStyleSheet("background-color: rgba(33, 45, 76, 150);")
        self.frame_top_btns_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_btns_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_btns_3.setObjectName("frame_top_btns_3")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_top_btns_3)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.frame_label_top_btns_3 = QtWidgets.QFrame(self.frame_top_btns_3)
        self.frame_label_top_btns_3.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_label_top_btns_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_top_btns_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_top_btns_3.setObjectName("frame_label_top_btns_3")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_label_top_btns_3)
        self.horizontalLayout_24.setContentsMargins(8, 0, 10, 0)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.frame_icon_top_bar_3 = QtWidgets.QFrame(self.frame_label_top_btns_3)
        self.frame_icon_top_bar_3.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_icon_top_bar_3.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_icon_top_bar_3.setStyleSheet("background: transparent;\n"
"image: url(images/shutter_speed_white_24dp.svg);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.frame_icon_top_bar_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_icon_top_bar_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_icon_top_bar_3.setObjectName("frame_icon_top_bar_3")
        self.horizontalLayout_24.addWidget(self.frame_icon_top_bar_3)
        self.label_title_bar_top_3 = QtWidgets.QLabel(self.frame_label_top_btns_3)
        self.label_title_bar_top_3.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_title_bar_top_3.setFont(font)
        self.label_title_bar_top_3.setStyleSheet("background: transparent;\n"
"margin-left: 5px;\n"
"color: rgb(255, 255, 255);")
        self.label_title_bar_top_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_bar_top_3.setObjectName("label_title_bar_top_3")
        self.horizontalLayout_24.addWidget(self.label_title_bar_top_3)
        self.horizontalLayout_23.addWidget(self.frame_label_top_btns_3)
        self.frame_btns_right_3 = QtWidgets.QFrame(self.frame_top_btns_3)
        self.frame_btns_right_3.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_btns_right_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btns_right_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns_right_3.setObjectName("frame_btns_right_3")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_btns_right_3)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.btn_minimize_3 = QtWidgets.QPushButton(self.frame_btns_right_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minimize_3.sizePolicy().hasHeightForWidth())
        self.btn_minimize_3.setSizePolicy(sizePolicy)
        self.btn_minimize_3.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_minimize_3.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_minimize_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Quorra\\Python-Projects\\Sorting-Algorithms-Visualisation\\qt_designer_ozan\\../images/minimize_white_24dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize_3.setIcon(icon)
        self.btn_minimize_3.setObjectName("btn_minimize_3")
        self.horizontalLayout_25.addWidget(self.btn_minimize_3)
        self.btn_maximize_restore_3 = QtWidgets.QPushButton(self.frame_btns_right_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_maximize_restore_3.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore_3.setSizePolicy(sizePolicy)
        self.btn_maximize_restore_3.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_maximize_restore_3.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_maximize_restore_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\Quorra\\Python-Projects\\Sorting-Algorithms-Visualisation\\qt_designer_ozan\\../images/open_in_full_white_24dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_maximize_restore_3.setIcon(icon1)
        self.btn_maximize_restore_3.setObjectName("btn_maximize_restore_3")
        self.horizontalLayout_25.addWidget(self.btn_maximize_restore_3)
        self.btn_close_3 = QtWidgets.QPushButton(self.frame_btns_right_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close_3.sizePolicy().hasHeightForWidth())
        self.btn_close_3.setSizePolicy(sizePolicy)
        self.btn_close_3.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_close_3.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_close_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\Quorra\\Python-Projects\\Sorting-Algorithms-Visualisation\\qt_designer_ozan\\../images/close_white_24dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close_3.setIcon(icon2)
        self.btn_close_3.setObjectName("btn_close_3")
        self.horizontalLayout_25.addWidget(self.btn_close_3)
        self.horizontalLayout_23.addWidget(self.frame_btns_right_3)
        self.verticalLayout_17.addWidget(self.frame_top_btns_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem)
        self.horizontalLayout_22.addWidget(self.frame_top_right_3)
        self.frame_main_binary.addWidget(self.frame_top_binary)
        self.frame_center_binary = QtWidgets.QVBoxLayout()
        self.frame_center_binary.setObjectName("frame_center_binary")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.MplSort = MplSort(self.centralwidget)
        self.MplSort.setMinimumSize(QtCore.QSize(910, 331))
        self.MplSort.setMaximumSize(QtCore.QSize(911, 331))
        self.MplSort.setObjectName("MplSort")
        self.horizontalLayout_2.addWidget(self.MplSort)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.frame_center_binary.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.disp_unsorted_array = QtWidgets.QTextEdit(self.centralwidget)
        self.disp_unsorted_array.setMinimumSize(QtCore.QSize(511, 91))
        self.disp_unsorted_array.setMaximumSize(QtCore.QSize(511, 91))
        self.disp_unsorted_array.setStyleSheet("background-color: rgb(252, 248, 232);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border 10 px;")
        self.disp_unsorted_array.setReadOnly(False)
        self.disp_unsorted_array.setObjectName("disp_unsorted_array")
        self.verticalLayout_3.addWidget(self.disp_unsorted_array)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.disp_sorted_array = QtWidgets.QTextEdit(self.centralwidget)
        self.disp_sorted_array.setMinimumSize(QtCore.QSize(511, 101))
        self.disp_sorted_array.setMaximumSize(QtCore.QSize(511, 101))
        self.disp_sorted_array.setStyleSheet("background-color: rgb(252, 248, 232);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.disp_sorted_array.setReadOnly(True)
        self.disp_sorted_array.setObjectName("disp_sorted_array")
        self.verticalLayout_4.addWidget(self.disp_sorted_array)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_10.addLayout(self.verticalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(100, 14))
        self.label_3.setMaximumSize(QtCore.QSize(100, 14))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.array_len = QtWidgets.QDial(self.centralwidget)
        self.array_len.setMinimumSize(QtCore.QSize(100, 99))
        self.array_len.setMaximumSize(QtCore.QSize(100, 99))
        self.array_len.setStyleSheet("background-color:rgba(120, 2, 6, 255);\n"
"\n"
"")
        self.array_len.setObjectName("array_len")
        self.verticalLayout_2.addWidget(self.array_len, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem5)
        self.display_arraylen = QtWidgets.QTextEdit(self.centralwidget)
        self.display_arraylen.setMinimumSize(QtCore.QSize(101, 31))
        self.display_arraylen.setMaximumSize(QtCore.QSize(101, 31))
        self.display_arraylen.setStyleSheet("background-color: rgb(252, 248, 232);")
        self.display_arraylen.setReadOnly(True)
        self.display_arraylen.setObjectName("display_arraylen")
        self.verticalLayout_8.addWidget(self.display_arraylen)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem6)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem7)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(101, 21))
        self.label_5.setMaximumSize(QtCore.QSize(101, 21))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lower_range = QtWidgets.QLineEdit(self.centralwidget)
        self.lower_range.setMinimumSize(QtCore.QSize(101, 31))
        self.lower_range.setMaximumSize(QtCore.QSize(101, 31))
        self.lower_range.setStyleSheet("background-color: rgb(252, 248, 232);")
        self.lower_range.setAlignment(QtCore.Qt.AlignCenter)
        self.lower_range.setObjectName("lower_range")
        self.horizontalLayout_3.addWidget(self.lower_range)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setMinimumSize(QtCore.QSize(101, 21))
        self.label_9.setMaximumSize(QtCore.QSize(101, 21))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.upper_range = QtWidgets.QLineEdit(self.centralwidget)
        self.upper_range.setMinimumSize(QtCore.QSize(101, 31))
        self.upper_range.setMaximumSize(QtCore.QSize(101, 31))
        self.upper_range.setStyleSheet("background-color: rgb(252, 248, 232);")
        self.upper_range.setAlignment(QtCore.Qt.AlignCenter)
        self.upper_range.setObjectName("upper_range")
        self.horizontalLayout_4.addWidget(self.upper_range)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout_9.addLayout(self.verticalLayout_7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem8)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem9)
        self.horizontalLayout_11.addLayout(self.verticalLayout_10)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(8)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.set_default_values = QtWidgets.QPushButton(self.centralwidget)
        self.set_default_values.setMinimumSize(QtCore.QSize(151, 41))
        self.set_default_values.setMaximumSize(QtCore.QSize(151, 41))
        self.set_default_values.setStyleSheet("#set_default_values{background-color:rgba(120, 2, 6, 255);\n"
"font: 10pt \"MS Shell Dlg 2\" white;\n"
"border-radius: 10px ;\n"
"color: white;}\n"
"\n"
"#set_default_values:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.425318, x2:1, y2:0.341, stop:0 rgba(120, 2, 6, 255), stop:1 rgba(45, 4, 83, 255));}")
        self.set_default_values.setObjectName("set_default_values")
        self.verticalLayout_11.addWidget(self.set_default_values)
        self.createanarray_btn = QtWidgets.QPushButton(self.centralwidget)
        self.createanarray_btn.setMinimumSize(QtCore.QSize(151, 41))
        self.createanarray_btn.setMaximumSize(QtCore.QSize(151, 41))
        self.createanarray_btn.setStyleSheet("#createanarray_btn{\n"
"background-color: rgba(66, 132, 255,0.8);\n"
"font: 10pt \"MS Shell Dlg 2\" white;\n"
"border-radius: 10px ;\n"
"color: white;\n"
"}\n"
"\n"
"#createanarray_btn:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.425318, x2:1, y2:0.341, stop:0 rgba(120, 2, 6, 255), stop:1 rgba(45, 4, 83, 255));\n"
"}")
        self.createanarray_btn.setObjectName("createanarray_btn")
        self.verticalLayout_11.addWidget(self.createanarray_btn)
        self.sort_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sort_btn.setMinimumSize(QtCore.QSize(151, 41))
        self.sort_btn.setMaximumSize(QtCore.QSize(151, 41))
        self.sort_btn.setStyleSheet("#sort_btn{\n"
"background-color: rgba(66, 132, 255,0.8);\n"
"font: 10pt \"MS Shell Dlg 2\" white;\n"
"border-radius: 10px ;\n"
"color: white;\n"
"}\n"
"\n"
"#sort_btn:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.425318, x2:1, y2:0.341, stop:0 rgba(120, 2, 6, 255), stop:1 rgba(45, 4, 83, 255));\n"
"}")
        self.sort_btn.setObjectName("sort_btn")
        self.verticalLayout_11.addWidget(self.sort_btn)
        self.horizontalLayout_7.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem11)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setMinimumSize(QtCore.QSize(164, 20))
        self.checkBox_2.setMaximumSize(QtCore.QSize(164, 20))
        self.checkBox_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color:black;")
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_6.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setMinimumSize(QtCore.QSize(164, 20))
        self.checkBox.setMaximumSize(QtCore.QSize(164, 20))
        self.checkBox.setToolTip("")
        self.checkBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color:black;")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_6.addWidget(self.checkBox)
        self.verticalLayout_12.addLayout(self.verticalLayout_6)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem12)
        self.horizontalLayout_7.addLayout(self.verticalLayout_12)
        self.verticalLayout_14.addLayout(self.horizontalLayout_7)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setSpacing(16)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem13)
        self.take_number = QtWidgets.QLineEdit(self.centralwidget)
        self.take_number.setMinimumSize(QtCore.QSize(171, 41))
        self.take_number.setMaximumSize(QtCore.QSize(171, 41))
        self.take_number.setStyleSheet("background-color: rgb(252, 248, 232);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.take_number.setAlignment(QtCore.Qt.AlignCenter)
        self.take_number.setObjectName("take_number")
        self.horizontalLayout_8.addWidget(self.take_number)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem14)
        self.verticalLayout_13.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem15)
        self.find_btn = QtWidgets.QPushButton(self.centralwidget)
        self.find_btn.setMinimumSize(QtCore.QSize(151, 41))
        self.find_btn.setMaximumSize(QtCore.QSize(151, 41))
        self.find_btn.setStyleSheet("#find_btn{\n"
"background-color: rgba(120, 2, 6, 255);\n"
"font: 10pt \"MS Shell Dlg 2\" white;\n"
"border-radius: 10px ;\n"
"color: white;\n"
"}\n"
"\n"
"#find_btn:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.425318, x2:1, y2:0.341, stop:0 rgba(120, 2, 6, 255), stop:1 rgba(45, 4, 83, 255));\n"
"}")
        self.find_btn.setObjectName("find_btn")
        self.horizontalLayout_9.addWidget(self.find_btn)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem16)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        self.result_edit = QtWidgets.QLabel(self.centralwidget)
        self.result_edit.setMinimumSize(QtCore.QSize(341, 51))
        self.result_edit.setMaximumSize(QtCore.QSize(341, 51))
        self.result_edit.setStyleSheet("background-color: rgb(252, 248, 232);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 0, 0);")
        self.result_edit.setText("")
        self.result_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.result_edit.setObjectName("result_edit")
        self.verticalLayout_13.addWidget(self.result_edit)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem17)
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setMinimumSize(QtCore.QSize(151, 41))
        self.clear_btn.setMaximumSize(QtCore.QSize(151, 41))
        self.clear_btn.setStyleSheet("#clear_btn{\n"
"background-color: rgba(66, 132, 255,0.8);\n"
"font: 10pt \"MS Shell Dlg 2\" white;\n"
"border-radius: 10px ;\n"
"color: white;\n"
"}\n"
"\n"
"#clear_btn:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.425318, x2:1, y2:0.341, stop:0 rgba(120, 2, 6, 255), stop:1 rgba(45, 4, 83, 255));\n"
"}")
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout_10.addWidget(self.clear_btn)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem18)
        self.verticalLayout_13.addLayout(self.horizontalLayout_10)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem19)
        self.verticalLayout_14.addLayout(self.verticalLayout_13)
        self.horizontalLayout_11.addLayout(self.verticalLayout_14)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem20)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 36)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem21)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.mic_btn = QtWidgets.QPushButton(self.centralwidget)
        self.mic_btn.setStyleSheet("#mic_btn{background-color: rgba(0,0,0,0);}\n"
"\n"
"#mic_btn:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.453136, x2:1, y2:0.523273, stop:0 rgba(104, 113, 138, 255), stop:1 rgba(215, 221, 232, 255));}")
        self.mic_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/microphone.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mic_btn.setIcon(icon3)
        self.mic_btn.setIconSize(QtCore.QSize(50, 50))
        self.mic_btn.setObjectName("mic_btn")
        self.horizontalLayout_13.addWidget(self.mic_btn)
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setStyleSheet("#back_btn{background-color: rgba(0,0,0,0);}\n"
"\n"
"#back_btn:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.453136, x2:1, y2:0.523273, stop:0 rgba(104, 113, 138, 255), stop:1 rgba(215, 221, 232, 255));}")
        self.back_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/images/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon4)
        self.back_btn.setIconSize(QtCore.QSize(60, 60))
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout_13.addWidget(self.back_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12.addLayout(self.verticalLayout)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem22)
        self.frame_center_binary.addLayout(self.horizontalLayout_12)
        self.frame_main_binary.addLayout(self.frame_center_binary)
        self.verticalLayout_18.addLayout(self.frame_main_binary)
        BinarySearchWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(BinarySearchWindow)
        self.statusBar.setObjectName("statusBar")
        BinarySearchWindow.setStatusBar(self.statusBar)

        self.retranslateUi(BinarySearchWindow)
        QtCore.QMetaObject.connectSlotsByName(BinarySearchWindow)

    def retranslateUi(self, BinarySearchWindow):
        _translate = QtCore.QCoreApplication.translate
        BinarySearchWindow.setWindowTitle(_translate("BinarySearchWindow", "MainWindow"))
        self.label_title_bar_top_3.setText(_translate("BinarySearchWindow", "Algorithms Project GUI - Binary Search"))
        self.btn_minimize_3.setToolTip(_translate("BinarySearchWindow", "Minimize"))
        self.btn_maximize_restore_3.setToolTip(_translate("BinarySearchWindow", "Maximize"))
        self.btn_close_3.setToolTip(_translate("BinarySearchWindow", "Close"))
        self.label_4.setText(_translate("BinarySearchWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Unsorted Array:</span></p></body></html>"))
        self.disp_unsorted_array.setPlaceholderText(_translate("BinarySearchWindow", "Please enter an array with \',\'"))
        self.label_6.setText(_translate("BinarySearchWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Sorted Array:</span></p></body></html>"))
        self.disp_sorted_array.setHtml(_translate("BinarySearchWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("BinarySearchWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Array Size</span></p></body></html>"))
        self.array_len.setToolTip(_translate("BinarySearchWindow", "Set the Array Size"))
        self.display_arraylen.setHtml(_translate("BinarySearchWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("BinarySearchWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Lower Range:</span></p></body></html>"))
        self.lower_range.setToolTip(_translate("BinarySearchWindow", "Set Lower Range"))
        self.label_9.setText(_translate("BinarySearchWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Upper Range:</span></p></body></html>"))
        self.upper_range.setToolTip(_translate("BinarySearchWindow", "Set Upper Range"))
        self.set_default_values.setToolTip(_translate("BinarySearchWindow", "The program assigns values ??????to default."))
        self.set_default_values.setText(_translate("BinarySearchWindow", "SET DEFAULT"))
        self.createanarray_btn.setToolTip(_translate("BinarySearchWindow", "Create array with selected values."))
        self.createanarray_btn.setText(_translate("BinarySearchWindow", "CREATE ARRAY"))
        self.sort_btn.setToolTip(_translate("BinarySearchWindow", "Sort the generated arrays."))
        self.sort_btn.setText(_translate("BinarySearchWindow", "SORT"))
        self.checkBox_2.setText(_translate("BinarySearchWindow", "Create an Array yourself"))
        self.checkBox.setText(_translate("BinarySearchWindow", "Create Random Array"))
        self.find_btn.setToolTip(_translate("BinarySearchWindow", "Find the Searched Index."))
        self.find_btn.setText(_translate("BinarySearchWindow", "FIND INDEX"))
        self.clear_btn.setToolTip(_translate("BinarySearchWindow", "Clear all values."))
        self.clear_btn.setText(_translate("BinarySearchWindow", "CLEAR"))
        self.back_btn.setToolTip(_translate("BinarySearchWindow", "Back to Menu"))
from mplsort import MplSort
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BinarySearchWindow = QtWidgets.QMainWindow()
    ui = Ui_BinarySearchWindow()
    ui.setupUi(BinarySearchWindow)
    BinarySearchWindow.show()
    sys.exit(app.exec_())
