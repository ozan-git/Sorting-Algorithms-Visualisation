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
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setMaximumSize(QtCore.QSize(3600, 1920))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.193545, 1.0, 0.676)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 187, 114))
        gradient.setColorAt(1.0, QtGui.QColor(122, 89, 196))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.193545, 1.0, 0.676)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 187, 114))
        gradient.setColorAt(1.0, QtGui.QColor(122, 89, 196))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.193545, 1.0, 0.676)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 187, 114))
        gradient.setColorAt(1.0, QtGui.QColor(122, 89, 196))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.193545, 1.0, 0.676)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 187, 114))
        gradient.setColorAt(1.0, QtGui.QColor(122, 89, 196))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.193545, 1.0, 0.676)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 187, 114))
        gradient.setColorAt(1.0, QtGui.QColor(122, 89, 196))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.193545, 1.0, 0.676)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 187, 114))
        gradient.setColorAt(1.0, QtGui.QColor(122, 89, 196))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.193545, 1.0, 0.676)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 187, 114))
        gradient.setColorAt(1.0, QtGui.QColor(122, 89, 196))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.193545, 1.0, 0.676)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 187, 114))
        gradient.setColorAt(1.0, QtGui.QColor(122, 89, 196))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.193545, 1.0, 0.676)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 187, 114))
        gradient.setColorAt(1.0, QtGui.QColor(122, 89, 196))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("#MainWindow{\n"
"background-color: rgb(219, 240, 242);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.193545, x2:1, y2:0.676, stop:0 rgba(30, 187, 114, 255), stop:1 rgba(122, 89, 196, 255));\n"
"}")
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_main = QtWidgets.QVBoxLayout()
        self.frame_main.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.frame_main.setSpacing(27)
        self.frame_main.setObjectName("frame_main")
        self.frame_top = QtWidgets.QFrame(self.centralwidget)
        self.frame_top.setMinimumSize(QtCore.QSize(1180, 0))
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_top.setStyleSheet("background-color: transparent;")
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_top_right = QtWidgets.QFrame(self.frame_top)
        self.frame_top_right.setStyleSheet("background: transparent;")
        self.frame_top_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_right.setObjectName("frame_top_right")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_right)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_top_btns = QtWidgets.QFrame(self.frame_top_right)
        self.frame_top_btns.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_top_btns.setStyleSheet("background-color: rgba(33, 45, 76, 150);")
        self.frame_top_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_btns.setObjectName("frame_top_btns")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_label_top_btns = QtWidgets.QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_label_top_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_top_btns.setObjectName("frame_label_top_btns")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setContentsMargins(8, 0, 10, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
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
        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)
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
        self.horizontalLayout_10.addWidget(self.label_title_bar_top)
        self.label_title_bar_top.raise_()
        self.frame_icon_top_bar.raise_()
        self.horizontalLayout_8.addWidget(self.frame_label_top_btns)
        self.frame_btns_right = QtWidgets.QFrame(self.frame_top_btns)
        self.frame_btns_right.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns_right.setObjectName("frame_btns_right")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
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
        self.horizontalLayout_9.addWidget(self.btn_minimize)
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
        self.horizontalLayout_9.addWidget(self.btn_maximize_restore)
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
        self.horizontalLayout_9.addWidget(self.btn_close)
        self.btn_minimize.raise_()
        self.btn_close.raise_()
        self.btn_maximize_restore.raise_()
        self.horizontalLayout_8.addWidget(self.frame_btns_right)
        self.verticalLayout_4.addWidget(self.frame_top_btns)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_7.addWidget(self.frame_top_right)
        self.frame_main.addWidget(self.frame_top)
        self.frame_center = QtWidgets.QVBoxLayout()
        self.frame_center.setObjectName("frame_center")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(491, 211))
        self.pushButton.setMaximumSize(QtCore.QSize(491, 211))
        self.pushButton.setStyleSheet("#pushButton{background-color: rgba(255, 255, 255,0);\n"
"}\n"
"")
        self.pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/logo_english_university.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(491, 211))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_mail = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mail.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.pushButton_mail.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/images/icon_feed_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_mail.setIcon(icon4)
        self.pushButton_mail.setIconSize(QtCore.QSize(55, 55))
        self.pushButton_mail.setObjectName("pushButton_mail")
        self.horizontalLayout_4.addWidget(self.pushButton_mail)
        self.pushButton_information = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_information.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_information.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.pushButton_information.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/images/icon_information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_information.setIcon(icon5)
        self.pushButton_information.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_information.setObjectName("pushButton_information")
        self.horizontalLayout_4.addWidget(self.pushButton_information)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.mic_btn = QtWidgets.QPushButton(self.centralwidget)
        self.mic_btn.setMinimumSize(QtCore.QSize(62, 62))
        self.mic_btn.setMaximumSize(QtCore.QSize(62, 62))
        self.mic_btn.setStyleSheet("#mic_btn{background-color: rgba(0,0,0,0);}\n"
"\n"
"#mic_btn:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.453136, x2:1, y2:0.523273, stop:0 rgba(104, 113, 138, 255), stop:1 rgba(215, 221, 232, 255));}")
        self.mic_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/images/microphone.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mic_btn.setIcon(icon6)
        self.mic_btn.setIconSize(QtCore.QSize(50, 50))
        self.mic_btn.setObjectName("mic_btn")
        self.horizontalLayout.addWidget(self.mic_btn)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.frame_center.addLayout(self.horizontalLayout_6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.frame_center.addItem(spacerItem7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.sort_button = QtWidgets.QPushButton(self.centralwidget)
        self.sort_button.setMinimumSize(QtCore.QSize(256, 128))
        self.sort_button.setMaximumSize(QtCore.QSize(224, 128))
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
        self.horizontalLayout_5.addWidget(self.sort_button)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.binary_search_button = QtWidgets.QPushButton(self.centralwidget)
        self.binary_search_button.setMinimumSize(QtCore.QSize(256, 128))
        self.binary_search_button.setMaximumSize(QtCore.QSize(256, 128))
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
        self.horizontalLayout_5.addWidget(self.binary_search_button)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.fibonacci_button = QtWidgets.QPushButton(self.centralwidget)
        self.fibonacci_button.setMinimumSize(QtCore.QSize(256, 128))
        self.fibonacci_button.setMaximumSize(QtCore.QSize(256, 128))
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
        self.horizontalLayout_5.addWidget(self.fibonacci_button)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.frame_center.addLayout(self.horizontalLayout_5)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.frame_center.addItem(spacerItem12)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.timecomp_button = QtWidgets.QPushButton(self.centralwidget)
        self.timecomp_button.setMinimumSize(QtCore.QSize(256, 128))
        self.timecomp_button.setMaximumSize(QtCore.QSize(256, 128))
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
        self.horizontalLayout_2.addWidget(self.timecomp_button)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.matrix_button = QtWidgets.QPushButton(self.centralwidget)
        self.matrix_button.setMinimumSize(QtCore.QSize(256, 128))
        self.matrix_button.setMaximumSize(QtCore.QSize(256, 128))
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
        self.horizontalLayout_2.addWidget(self.matrix_button)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem15)
        self.kthsmallest_button = QtWidgets.QPushButton(self.centralwidget)
        self.kthsmallest_button.setMinimumSize(QtCore.QSize(256, 128))
        self.kthsmallest_button.setMaximumSize(QtCore.QSize(256, 128))
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
        self.horizontalLayout_2.addWidget(self.kthsmallest_button)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem16)
        self.frame_center.addLayout(self.horizontalLayout_2)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.frame_center.addItem(spacerItem17)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem18)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(564, 61))
        self.pushButton_2.setMaximumSize(QtCore.QSize(564, 61))
        self.pushButton_2.setStyleSheet("#pushButton_2{background-color: rgba(255, 255, 255,0);\n"
"}\n"
"")
        self.pushButton_2.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/images/created_by_ozan.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon7)
        self.pushButton_2.setIconSize(QtCore.QSize(564, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem19)
        self.frame_center.addLayout(self.horizontalLayout_3)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.frame_center.addItem(spacerItem20)
        self.size_grip = QtWidgets.QFrame(self.centralwidget)
        self.size_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.size_grip.setObjectName("size_grip")
        self.frame_center.addWidget(self.size_grip)
        self.frame_main.addLayout(self.frame_center)
        self.verticalLayout_2.addLayout(self.frame_main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title_bar_top.setText(_translate("MainWindow", "Algorithms Project GUI - Home Page"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_maximize_restore.setToolTip(_translate("MainWindow", "Maximize"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Visit Izmir Katip Celebi University website.</p></body></html>"))
        self.pushButton_mail.setToolTip(_translate("MainWindow", "Send Feedback"))
        self.pushButton_information.setToolTip(_translate("MainWindow", "Get Information"))
        self.sort_button.setText(_translate("MainWindow", "SORTING ALGORITHMS"))
        self.binary_search_button.setText(_translate("MainWindow", "BINARY SEARCH"))
        self.fibonacci_button.setText(_translate("MainWindow", "FIBONACCI NUMBER"))
        self.timecomp_button.setText(_translate("MainWindow", "TIME COMPARISON"))
        self.matrix_button.setText(_translate("MainWindow", "MATRIX MULTIPLICATION"))
        self.kthsmallest_button.setText(_translate("MainWindow", "RANDOMIZED SELECTION"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
