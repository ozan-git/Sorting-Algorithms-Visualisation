# -*- coding: utf-8 -*-
"""
Created on Tue November 30 9:14 PM 2021

Created by Orhan Ozan Yildiz
"""
from PyQt5.QtWidgets import QMainWindow

from main_sort_gui import SortingAlgorithms
from main_ui_algorithms_project_uicodes import Ui_MainWindow


class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle('Home')
		self.sort_main = SortingAlgorithms()
		self.main_matrix_mult = matrix_multiplication()