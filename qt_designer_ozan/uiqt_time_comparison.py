# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Quorra\Python-Projects\Sorting-Algorithms-Visualisation\qt_designer_ozan\time_comparison_uiqt.ui'
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
        MainWindow.setMaximumSize(QtCore.QSize(1200, 900))
        MainWindow.setStyleSheet("#MainWindow{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.193545, x2:1, y2:0.676, stop:0 rgba(30, 187, 114, 255), stop:1 rgba(122, 89, 196, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(1080, 30, 61, 51))
        self.back_btn.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.back_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setIconSize(QtCore.QSize(60, 60))
        self.back_btn.setObjectName("back_btn")
        self.MplSort = MplSort(self.centralwidget)
        self.MplSort.setGeometry(QtCore.QRect(140, 60, 901, 351))
        self.MplSort.setObjectName("MplSort")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(550, 430, 124, 36))
        self.clear_btn.setMinimumSize(QtCore.QSize(124, 36))
        self.clear_btn.setMaximumSize(QtCore.QSize(124, 36))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.clear_btn.setFont(font)
        self.clear_btn.setStyleSheet("#clear_btn{\n"
"background-color: rgb(102, 61, 54);\n"
"border-radius: 10px ;\n"
"color: white;}\n"
"\n"
"#clear_btn:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.625, y2:0.761, stop:0 rgba(48, 33, 14, 255), stop:1 rgba(0, 108, 80, 255));\n"
"}")
        self.clear_btn.setObjectName("clear_btn")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 10, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(680, 510, 387, 186))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(24)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(18)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bubblesort_checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bubblesort_checkBox.setFont(font)
        self.bubblesort_checkBox.setStyleSheet("bubblesort_checkBox{\n"
"\n"
"}")
        self.bubblesort_checkBox.setObjectName("bubblesort_checkBox")
        self.verticalLayout.addWidget(self.bubblesort_checkBox)
        self.insertionsort_checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.insertionsort_checkBox.setFont(font)
        self.insertionsort_checkBox.setObjectName("insertionsort_checkBox")
        self.verticalLayout.addWidget(self.insertionsort_checkBox)
        self.mergesort_checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mergesort_checkBox.setFont(font)
        self.mergesort_checkBox.setObjectName("mergesort_checkBox")
        self.verticalLayout.addWidget(self.mergesort_checkBox)
        self.heapsort_checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.heapsort_checkBox.setFont(font)
        self.heapsort_checkBox.setObjectName("heapsort_checkBox")
        self.verticalLayout.addWidget(self.heapsort_checkBox)
        self.selectionsort_checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.selectionsort_checkBox.setFont(font)
        self.selectionsort_checkBox.setObjectName("selectionsort_checkBox")
        self.verticalLayout.addWidget(self.selectionsort_checkBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.quicksort_checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.quicksort_checkBox.setFont(font)
        self.quicksort_checkBox.setObjectName("quicksort_checkBox")
        self.verticalLayout_2.addWidget(self.quicksort_checkBox)
        self.bucketsort_checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bucketsort_checkBox.setFont(font)
        self.bucketsort_checkBox.setObjectName("bucketsort_checkBox")
        self.verticalLayout_2.addWidget(self.bucketsort_checkBox)
        self.countingsort_checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.countingsort_checkBox.setFont(font)
        self.countingsort_checkBox.setObjectName("countingsort_checkBox")
        self.verticalLayout_2.addWidget(self.countingsort_checkBox)
        self.radixsort_checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radixsort_checkBox.setFont(font)
        self.radixsort_checkBox.setObjectName("radixsort_checkBox")
        self.verticalLayout_2.addWidget(self.radixsort_checkBox)
        self.shellsort_checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.shellsort_checkBox.setFont(font)
        self.shellsort_checkBox.setObjectName("shellsort_checkBox")
        self.verticalLayout_2.addWidget(self.shellsort_checkBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(260, 510, 322, 109))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(24)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comparisonall_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.comparisonall_button.setMinimumSize(QtCore.QSize(320, 36))
        self.comparisonall_button.setMaximumSize(QtCore.QSize(320, 36))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.comparisonall_button.setFont(font)
        self.comparisonall_button.setStyleSheet("#comparisonall_button{\n"
"background-color: rgb(102, 61, 54);\n"
"border-radius: 10px ;\n"
"color: white;\n"
"}\n"
"\n"
"#comparisonall_button:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.625, y2:0.761, stop:0 rgba(48, 33, 14, 255), stop:1 rgba(0, 108, 80, 255));\n"
"}")
        self.comparisonall_button.setObjectName("comparisonall_button")
        self.verticalLayout_3.addWidget(self.comparisonall_button)
        self.comparisonchoosen_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.comparisonchoosen_button.setMinimumSize(QtCore.QSize(320, 40))
        self.comparisonchoosen_button.setMaximumSize(QtCore.QSize(320, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comparisonchoosen_button.setFont(font)
        self.comparisonchoosen_button.setStyleSheet("#comparisonchoosen_button{\n"
"background-color: rgb(102, 61, 54);\n"
"border-radius: 10px ;\n"
"color: white;\n"
"}\n"
"\n"
"#comparisonchoosen_button:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.625, y2:0.761, stop:0 rgba(48, 33, 14, 255), stop:1 rgba(0, 108, 80, 255));\n"
"}")
        self.comparisonchoosen_button.setObjectName("comparisonchoosen_button")
        self.verticalLayout_3.addWidget(self.comparisonchoosen_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.back_btn.setToolTip(_translate("MainWindow", "Back To Menu"))
        self.clear_btn.setText(_translate("MainWindow", "CLEAR"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-style:italic; color:#000000;\">Time Comparison</span></p></body></html>"))
        self.bubblesort_checkBox.setText(_translate("MainWindow", "BUBBLE SORT"))
        self.insertionsort_checkBox.setText(_translate("MainWindow", "INSERTION SORT"))
        self.mergesort_checkBox.setText(_translate("MainWindow", "MERGE SORT"))
        self.heapsort_checkBox.setText(_translate("MainWindow", "HEAP SORT"))
        self.selectionsort_checkBox.setText(_translate("MainWindow", "SELECTION SORT"))
        self.quicksort_checkBox.setText(_translate("MainWindow", "QUICK SORT"))
        self.bucketsort_checkBox.setText(_translate("MainWindow", "BUCKET SORT"))
        self.countingsort_checkBox.setText(_translate("MainWindow", "COUNTING SORT"))
        self.radixsort_checkBox.setText(_translate("MainWindow", "RADIX SORT"))
        self.shellsort_checkBox.setText(_translate("MainWindow", "SHELL SORT"))
        self.comparisonall_button.setText(_translate("MainWindow", "COMPARISON ALL"))
        self.comparisonchoosen_button.setText(_translate("MainWindow", "COMPARISON CHOOSEN"))
from mplsort import MplSort
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
