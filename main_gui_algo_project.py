# Introduction to Algorithm course graphical interface design project home page.
# 5 December 2021.

# Written by Orhan Ozan Yildiz.

import sys
import webbrowser

import speech_recognition as sr
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget
from PyQt5.QtWidgets import QMessageBox
from iconify.qt import QtCore

from main_gui_binary_search import BinarySearch
from main_gui_fibonacci import Fibonacci
from main_gui_help import HelpWindow
from main_gui_matrix_operations import MatrixOperation
from main_gui_randomized_selection import RandomizedSelection
from main_gui_sort import SortingAlgorithms
from main_gui_time_comparison import TimeComparisonMainWindow
from uiqt_main import Ui_MainWindow


def add_ikc_link():
	webbrowser.open('https://www.ikcu.edu.tr/')


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle('Home')
		self.sort_main = SortingAlgorithms()
		self.main_matrix_operation = MatrixOperation()
		self.fibonacci_main = Fibonacci()
		self.binary_search_main = BinarySearch()
		self.randomized_selection_main = RandomizedSelection()
		self.time_comparison_main = TimeComparisonMainWindow()
		self.help_main = HelpWindow()

		self.ui.sort_button.clicked.connect(self.sort_operations)
		self.ui.matrix_button.clicked.connect(self.matrix_operations)
		self.ui.fibonacci_button.clicked.connect(self.fibonacci_operations)
		self.ui.binary_search_button.clicked.connect(self.binary_search_operations)
		self.ui.kthsmallest_button.clicked.connect(self.randomized_selection_operations)
		self.ui.timecomp_button.clicked.connect(self.time_comparison_operations)
		self.ui.pushButton_information.clicked.connect(self.help_operations)
		self.ui.pushButton.clicked.connect(add_ikc_link)
		self.ui.pushButton_mail.clicked.connect(self.sendmail)
		self.subject = 'The features I specified can be added to the Introduction to algorithm project.'
		self.ui.mic_btn.clicked.connect(self.voice)
		self.ui.btn_close.clicked.connect(self.close)
		self.ui.btn_maximize_restore.clicked.connect(self.showMaximized)
		self.ui.btn_minimize.clicked.connect(self.showMinimized)

		self.setWindowFlags(Qt.CustomizeWindowHint)
		self.pressing = False

	def resizeEvent(self, QResizeEvent):
		super(MainWindow, self).resizeEvent(QResizeEvent)
		self.ui.frame_top.setFixedWidth(self.width())

	def mousePressEvent(self, event):
		self.start = self.mapToGlobal(event.pos())
		self.pressing = True

	def mouseMoveEvent(self, event):
		if self.pressing:
			self.end = self.mapToGlobal(event.pos())
			self.movement = self.end - self.start
			self.setGeometry(self.mapToGlobal(self.movement).x(),
							 self.mapToGlobal(self.movement).y(),
							 self.width(),
							 self.height())
			self.start = self.end

	def mouseReleaseEvent(self, QMouseEvent):
		self.pressing = False

	def sendmail(self):
		webbrowser.open('mailto:orhan.ozan351@gmail.com?' + '&subject=' + self.subject, new=1)

	def sort_operations(self):
		self.sort_main.clear()
		self.sort_main.show()

	def matrix_operations(self):
		self.main_matrix_operation.clear()
		self.main_matrix_operation.show()

	def fibonacci_operations(self):
		# self.fibonacci_main.clear()
		self.fibonacci_main.show()

	def binary_search_operations(self):
		self.binary_search_main.clear()
		self.binary_search_main.show()

	def randomized_selection_operations(self):
		self.randomized_selection_main.clear()
		self.randomized_selection_main.show()

	def time_comparison_operations(self):
		self.time_comparison_main.clear()
		self.time_comparison_main.show()

	def help_operations(self):
		self.help_main.show()

	#
	# def resizeEvent(self, QResizeEvent):
	# 	super(self).resizeEvent(QResizeEvent)
	# 	self.title.setFixedWidth(self.width())
	#
	# def mousePressEvent(self, event):
	# 	self.start = self.mapToGlobal(event.pos())
	# 	self.pressing = True
	#
	# def mouseMoveEvent(self, event):
	# 	if self.pressing:
	# 		self.end = self.mapToGlobal(event.pos())
	# 		self.movement = self.end - self.start
	# 		self.setGeometry(self.mapToGlobal(self.movement).x(), self.mapToGlobal(self.movement).y(), self.width(),
	# 						 self.height())
	# 		self.start = self.end
	#
	# def mouseReleaseEvent(self, QMouseEvent):
	# 	self.pressing = False
	#
	# def btn_max_clicked(self):
	# 	self.showMaximized()
	#
	# def btn_min_clicked(self):
	# 	self.showMinimized()
	#
	def btn_close_clicked(self):
		self.close()

	def voice(self):
		reader_voice = sr.Recognizer()
		# microphoneValue = ""
		with sr.Microphone() as source:
			try:
				self.statusBar().showMessage('Start talking...')
				audio = reader_voice.listen(source)
				microphoneValue = (reader_voice.recognize_google(audio))
				self.statusBar().showMessage('Stop talking...')
				print(microphoneValue)
				try:
					if microphoneValue == 'sorting algorithms':
						try:
							self.sort_operations()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")

					elif microphoneValue == 'matrix multiplication':
						try:
							self.matrix_operations()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")
					elif microphoneValue == 'time comparison':
						try:
							self.time_comparison_operations()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")
					elif microphoneValue == 'Fibonacci number':
						try:
							self.fibonacci_operations()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")
					elif microphoneValue == 'binary search':
						try:
							self.binary_search_operations()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")
					elif microphoneValue == 'randomized selection':
						try:
							self.randomized_selection_operations()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")
					elif microphoneValue == 'close':
						try:
							self.close()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")
					elif microphoneValue == 'help':
						try:
							self.help_operations()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")
					elif microphoneValue == 'LinkedIn':
						try:
							self.addlinkedinlink()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")
					elif microphoneValue == 'YouTube':
						try:
							self.addyoutubelink()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")

					elif microphoneValue == 'send email':
						try:
							self.sendmail()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")
					else:
						QMessageBox.warning(self, "ERROR", "Try Again...")
				except:
					QMessageBox.warning(self, "ERROR", "Try again...")
			except sr.UnknownValueError:
				QMessageBox.information(self, "ERROR", "Sorry, Cant understand, Please say again..")
			except sr.RequestError as e:
				QMessageBox.information(self, "ERROR",
										"Could not request results from Google Speech Recognition service; {0}".format(
											e))
			except sr.RequestError:
				QMessageBox.information(self, "ERROR", "No Internet Connection...")


# %% Initialization
if __name__ == "__main__":
	app = QApplication([])
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
