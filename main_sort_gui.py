from PyQt5.QtWidgets import QMainWindow

from sorting_ui_algorithms_project_uicodes import Ui_SortWindow


class SortingAlgorithms(QMainWindow):
	stop_array = "global"

	def __init__(self):
		super().__init__()
		self.ui = Ui_SortWindow()