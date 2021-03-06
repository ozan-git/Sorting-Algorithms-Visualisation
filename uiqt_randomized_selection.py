# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Quorra\Python-Projects\Sorting-Algorithms-Visualisation\qt_designer_ozan\randomized_selection_uiqt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RandomizedSelectionWindow(object):
    def setupUi(self, RandomizedSelectionWindow):
        RandomizedSelectionWindow.setObjectName("RandomizedSelectionWindow")
        RandomizedSelectionWindow.resize(1200, 800)
        RandomizedSelectionWindow.setMinimumSize(QtCore.QSize(1200, 800))
        RandomizedSelectionWindow.setMaximumSize(QtCore.QSize(365686, 868686))
        RandomizedSelectionWindow.setStyleSheet("#RandomizedSelectionWindow{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.193545, x2:1, y2:0.676, stop:0 rgba(30, 187, 114, 255), stop:1 rgba(122, 89, 196, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(RandomizedSelectionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_top = QtWidgets.QFrame(self.centralwidget)
        self.frame_top.setMinimumSize(QtCore.QSize(1180, 0))
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_top.setStyleSheet("background-color: transparent;")
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.frame_top_right = QtWidgets.QFrame(self.frame_top)
        self.frame_top_right.setStyleSheet("background: transparent;")
        self.frame_top_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_right.setObjectName("frame_top_right")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_top_right)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_top_btns = QtWidgets.QFrame(self.frame_top_right)
        self.frame_top_btns.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_top_btns.setStyleSheet("background-color: rgba(33, 45, 76, 150);")
        self.frame_top_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_btns.setObjectName("frame_top_btns")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.frame_label_top_btns = QtWidgets.QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_label_top_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_top_btns.setObjectName("frame_label_top_btns")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_29.setContentsMargins(8, 0, 10, 0)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.frame_icon_top_bar = QtWidgets.QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_icon_top_bar.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet("background: transparent;\n"
"image: url(images/shutter_speed_white_24dp.svg);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.frame_icon_top_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_icon_top_bar.setObjectName("frame_icon_top_bar")
        self.horizontalLayout_29.addWidget(self.frame_icon_top_bar)
        self.label_title_bar_top = QtWidgets.QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setStyleSheet("background: transparent;\n"
"margin-left: 5px;\n"
"color: rgb(255, 255, 255);")
        self.label_title_bar_top.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_bar_top.setObjectName("label_title_bar_top")
        self.horizontalLayout_29.addWidget(self.label_title_bar_top)
        self.label_title_bar_top.raise_()
        self.frame_icon_top_bar.raise_()
        self.horizontalLayout_28.addWidget(self.frame_label_top_btns)
        self.frame_btns_right = QtWidgets.QFrame(self.frame_top_btns)
        self.frame_btns_right.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns_right.setObjectName("frame_btns_right")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_minimize.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_minimize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Quorra\\Python-Projects\\Sorting-Algorithms-Visualisation\\qt_designer_ozan\\../images/minimize_white_24dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon)
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_30.addWidget(self.btn_minimize)
        self.btn_maximize_restore = QtWidgets.QPushButton(self.frame_btns_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy)
        self.btn_maximize_restore.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_maximize_restore.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_maximize_restore.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\Quorra\\Python-Projects\\Sorting-Algorithms-Visualisation\\qt_designer_ozan\\../images/open_in_full_white_24dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)
        self.btn_maximize_restore.setObjectName("btn_maximize_restore")
        self.horizontalLayout_30.addWidget(self.btn_maximize_restore)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_close.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_close.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\Quorra\\Python-Projects\\Sorting-Algorithms-Visualisation\\qt_designer_ozan\\../images/close_white_24dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_30.addWidget(self.btn_close)
        self.btn_minimize.raise_()
        self.btn_close.raise_()
        self.btn_maximize_restore.raise_()
        self.horizontalLayout_28.addWidget(self.frame_btns_right)
        self.verticalLayout_17.addWidget(self.frame_top_btns)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem)
        self.horizontalLayout_27.addWidget(self.frame_top_right)
        self.verticalLayout_14.addWidget(self.frame_top)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.MplSort = MplSort(self.centralwidget)
        self.MplSort.setMinimumSize(QtCore.QSize(911, 331))
        self.MplSort.setMaximumSize(QtCore.QSize(911, 331))
        self.MplSort.setObjectName("MplSort")
        self.horizontalLayout_2.addWidget(self.MplSort)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_12.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(52, -1, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem3)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.disp_unsorted_array = QtWidgets.QTextEdit(self.centralwidget)
        self.disp_unsorted_array.setMinimumSize(QtCore.QSize(531, 91))
        self.disp_unsorted_array.setMaximumSize(QtCore.QSize(531, 91))
        self.disp_unsorted_array.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border 10 px;")
        self.disp_unsorted_array.setReadOnly(False)
        self.disp_unsorted_array.setObjectName("disp_unsorted_array")
        self.verticalLayout.addWidget(self.disp_unsorted_array)
        self.verticalLayout_9.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.disp_sorted_array = QtWidgets.QTextEdit(self.centralwidget)
        self.disp_sorted_array.setMinimumSize(QtCore.QSize(531, 101))
        self.disp_sorted_array.setMaximumSize(QtCore.QSize(531, 101))
        self.disp_sorted_array.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.disp_sorted_array.setReadOnly(True)
        self.disp_sorted_array.setObjectName("disp_sorted_array")
        self.verticalLayout_2.addWidget(self.disp_sorted_array)
        self.verticalLayout_9.addLayout(self.verticalLayout_2)
        self.verticalLayout_11.addLayout(self.verticalLayout_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.array_len = QtWidgets.QDial(self.centralwidget)
        self.array_len.setMinimumSize(QtCore.QSize(100, 100))
        self.array_len.setMaximumSize(QtCore.QSize(100, 100))
        self.array_len.setStyleSheet("background-color: rgba(120, 2, 6, 255);")
        self.array_len.setObjectName("array_len")
        self.verticalLayout_5.addWidget(self.array_len)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.display_arraylen = QtWidgets.QTextEdit(self.centralwidget)
        self.display_arraylen.setMinimumSize(QtCore.QSize(101, 31))
        self.display_arraylen.setMaximumSize(QtCore.QSize(101, 31))
        self.display_arraylen.setStyleSheet("")
        self.display_arraylen.setReadOnly(True)
        self.display_arraylen.setObjectName("display_arraylen")
        self.horizontalLayout_5.addWidget(self.display_arraylen)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lower_range = QtWidgets.QLineEdit(self.centralwidget)
        self.lower_range.setMinimumSize(QtCore.QSize(101, 31))
        self.lower_range.setMaximumSize(QtCore.QSize(101, 31))
        self.lower_range.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border 10 px;")
        self.lower_range.setAlignment(QtCore.Qt.AlignCenter)
        self.lower_range.setObjectName("lower_range")
        self.horizontalLayout_3.addWidget(self.lower_range)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.upper_range = QtWidgets.QLineEdit(self.centralwidget)
        self.upper_range.setMinimumSize(QtCore.QSize(101, 31))
        self.upper_range.setMaximumSize(QtCore.QSize(101, 31))
        self.upper_range.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border 10 px;")
        self.upper_range.setAlignment(QtCore.Qt.AlignCenter)
        self.upper_range.setObjectName("upper_range")
        self.horizontalLayout_4.addWidget(self.upper_range)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_11.addLayout(self.horizontalLayout_6)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem6)
        self.horizontalLayout_11.addLayout(self.verticalLayout_11)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.set_default_values = QtWidgets.QPushButton(self.centralwidget)
        self.set_default_values.setMinimumSize(QtCore.QSize(151, 41))
        self.set_default_values.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2 white")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.set_default_values.setFont(font)
        self.set_default_values.setStyleSheet("#set_default_values{\n"
"background-color: rgba(120, 2, 6, 255);\n"
"font: 12pt \"MS Shell Dlg 2\" white;\n"
"border-radius: 10px ;\n"
"color: white;}\n"
"\n"
"#set_default_values:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.425318, x2:1, y2:0.341, stop:0 rgba(120, 2, 6, 255), stop:1 rgba(45, 4, 83, 255));}")
        self.set_default_values.setObjectName("set_default_values")
        self.verticalLayout_4.addWidget(self.set_default_values)
        self.createanarray_btn = QtWidgets.QPushButton(self.centralwidget)
        self.createanarray_btn.setMinimumSize(QtCore.QSize(151, 41))
        self.createanarray_btn.setMaximumSize(QtCore.QSize(200, 100))
        self.createanarray_btn.setStyleSheet("#createanarray_btn{\n"
"background-color: rgba(66, 132, 255,0.8);\n"
"font: 12pt \"MS Shell Dlg 2\" white;\n"
"border-radius: 10px ;\n"
"color: white;\n"
"}\n"
"\n"
"#createanarray_btn:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.425318, x2:1, y2:0.341, stop:0 rgba(120, 2, 6, 255), stop:1 rgba(45, 4, 83, 255));\n"
"}")
        self.createanarray_btn.setObjectName("createanarray_btn")
        self.verticalLayout_4.addWidget(self.createanarray_btn)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem10)
        self.random_array_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.random_array_checkbox.setMinimumSize(QtCore.QSize(165, 20))
        self.random_array_checkbox.setMaximumSize(QtCore.QSize(165, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.random_array_checkbox.setFont(font)
        self.random_array_checkbox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.random_array_checkbox.setObjectName("random_array_checkbox")
        self.verticalLayout_7.addWidget(self.random_array_checkbox)
        self.create_array_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.create_array_checkbox.setMinimumSize(QtCore.QSize(165, 20))
        self.create_array_checkbox.setMaximumSize(QtCore.QSize(165, 20))
        self.create_array_checkbox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.create_array_checkbox.setObjectName("create_array_checkbox")
        self.verticalLayout_7.addWidget(self.create_array_checkbox)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem11)
        self.horizontalLayout_10.addLayout(self.verticalLayout_7)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.take_number = QtWidgets.QLineEdit(self.centralwidget)
        self.take_number.setMinimumSize(QtCore.QSize(171, 41))
        self.take_number.setMaximumSize(QtCore.QSize(171, 41))
        self.take_number.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.take_number.setAlignment(QtCore.Qt.AlignCenter)
        self.take_number.setObjectName("take_number")
        self.horizontalLayout_7.addWidget(self.take_number)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.find_btn = QtWidgets.QPushButton(self.centralwidget)
        self.find_btn.setMinimumSize(QtCore.QSize(151, 41))
        self.find_btn.setMaximumSize(QtCore.QSize(360, 60))
        self.find_btn.setStyleSheet("#find_btn{font: 12pt \"MS Shell Dlg 2\" white;\n"
"background-color: rgba(120, 2, 6, 255);\n"
"border-radius: 10px ;\n"
"color: white;}\n"
"#find_btn:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.425318, x2:1, y2:0.341, stop:0 rgba(120, 2, 6, 255), stop:1 rgba(45, 4, 83, 255));}")
        self.find_btn.setObjectName("find_btn")
        self.horizontalLayout_8.addWidget(self.find_btn)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.result_edit = QtWidgets.QLabel(self.centralwidget)
        self.result_edit.setMinimumSize(QtCore.QSize(341, 51))
        self.result_edit.setMaximumSize(QtCore.QSize(341, 51))
        self.result_edit.setStyleSheet("background-color: rgb(252, 248, 232);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 0, 0);")
        self.result_edit.setText("")
        self.result_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.result_edit.setObjectName("result_edit")
        self.verticalLayout_8.addWidget(self.result_edit)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem14)
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setMinimumSize(QtCore.QSize(151, 41))
        self.clear_btn.setMaximumSize(QtCore.QSize(151, 41))
        self.clear_btn.setStyleSheet("#clear_btn{\n"
"font: 12pt \"MS Shell Dlg 2\" white;\n"
"border-radius: 10px ;\n"
"background-color: rgba(66, 132, 255,0.8);\n"
"color: white;}\n"
"\n"
"#clear_btn:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.425318, x2:1, y2:0.341, stop:0 rgba(120, 2, 6, 255), stop:1 rgba(45, 4, 83, 255));}")
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout_9.addWidget(self.clear_btn)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem15)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.verticalLayout_10.addLayout(self.verticalLayout_8)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem16)
        self.horizontalLayout_11.addLayout(self.verticalLayout_10)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem17)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem18)
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
        self.verticalLayout_13.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12.addLayout(self.verticalLayout_13)
        self.verticalLayout_12.addLayout(self.horizontalLayout_12)
        self.verticalLayout_14.addLayout(self.verticalLayout_12)
        RandomizedSelectionWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RandomizedSelectionWindow)
        self.statusbar.setObjectName("statusbar")
        RandomizedSelectionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RandomizedSelectionWindow)
        QtCore.QMetaObject.connectSlotsByName(RandomizedSelectionWindow)

    def retranslateUi(self, RandomizedSelectionWindow):
        _translate = QtCore.QCoreApplication.translate
        RandomizedSelectionWindow.setWindowTitle(_translate("RandomizedSelectionWindow", "MainWindow"))
        self.label_title_bar_top.setText(_translate("RandomizedSelectionWindow", "Algorithms Project GUI - Randomized Selection"))
        self.btn_minimize.setToolTip(_translate("RandomizedSelectionWindow", "Minimize"))
        self.btn_maximize_restore.setToolTip(_translate("RandomizedSelectionWindow", "Maximize"))
        self.btn_close.setToolTip(_translate("RandomizedSelectionWindow", "Close"))
        self.label_3.setText(_translate("RandomizedSelectionWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Unsorted Array:</span></p></body></html>"))
        self.disp_unsorted_array.setPlaceholderText(_translate("RandomizedSelectionWindow", "Please enter an array with \',\' (i.e: 3,5,2,6,12,54):"))
        self.label_4.setText(_translate("RandomizedSelectionWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Sorted Array:</span></p></body></html>"))
        self.disp_sorted_array.setHtml(_translate("RandomizedSelectionWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("RandomizedSelectionWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Array Size</span></p></body></html>"))
        self.array_len.setToolTip(_translate("RandomizedSelectionWindow", "Set the Array Size"))
        self.display_arraylen.setHtml(_translate("RandomizedSelectionWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("RandomizedSelectionWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Lower Range:</span></p></body></html>"))
        self.lower_range.setToolTip(_translate("RandomizedSelectionWindow", "Set Lower Range"))
        self.label_9.setText(_translate("RandomizedSelectionWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Upper Range:</span></p></body></html>"))
        self.upper_range.setToolTip(_translate("RandomizedSelectionWindow", "Set Upper Range"))
        self.set_default_values.setToolTip(_translate("RandomizedSelectionWindow", "Create array with selected values."))
        self.set_default_values.setText(_translate("RandomizedSelectionWindow", "SET DEFAULT"))
        self.createanarray_btn.setToolTip(_translate("RandomizedSelectionWindow", "Create array with selected values."))
        self.createanarray_btn.setText(_translate("RandomizedSelectionWindow", "CREATE ARRAY"))
        self.random_array_checkbox.setText(_translate("RandomizedSelectionWindow", "Create Random Array"))
        self.create_array_checkbox.setText(_translate("RandomizedSelectionWindow", "Create an Array Yourself"))
        self.find_btn.setToolTip(_translate("RandomizedSelectionWindow", "Find the kth Smallest Index"))
        self.find_btn.setText(_translate("RandomizedSelectionWindow", "FIND I\'TH SMALLEST "))
        self.clear_btn.setToolTip(_translate("RandomizedSelectionWindow", "Clear all values."))
        self.clear_btn.setText(_translate("RandomizedSelectionWindow", "CLEAR"))
        self.back_btn.setToolTip(_translate("RandomizedSelectionWindow", "Back to Menu"))
from mplsort import MplSort
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RandomizedSelectionWindow = QtWidgets.QMainWindow()
    ui = Ui_RandomizedSelectionWindow()
    ui.setupUi(RandomizedSelectionWindow)
    RandomizedSelectionWindow.show()
    sys.exit(app.exec_())
