# Introduction to Algorithm course graphical interface design project binary search page.
# 5 December 2021.

# Written by Orhan Ozan Yildiz.
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDial
from PyQt5.QtGui import QIntValidator
import sys
from utils_operations import binarysearch
from uiqt_binary_search import Ui_BinarySearchWindow
import numpy as np
import time
import random
import speech_recognition as sr

binarySearch = binarysearch()


# %% Application Content
class BinarySearch(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_BinarySearchWindow()  # Ability to use the class in which the interface I designed with qt designer converted into code
		self.ui.setupUi(self)
		self.setWindowTitle('Binary Search')
		self.ui.array_len.setMinimum(0)  # Fixing the dial to min 1 max 50
		self.ui.array_len.setMaximum(50)
		# self.ui.range.valueChanged.connect(self.valuerange)                     #Link to print the number on the dial on the line edit next to it
		self.ui.array_len.valueChanged.connect(
			self.valuelen)  # Link to print the number on the dial on the line edit next to it
		self.ui.createanarray_btn.clicked.connect(
			self.create_array)  # Connecting the create array button with the corresponding function
		self.ui.back_btn.clicked.connect(self.close)  # back to main menu
		self.ui.sort_btn.clicked.connect(
			self.sortingarray)  # Connecting the sort button with the corresponding function
		self.ui.find_btn.clicked.connect(
			self.find_number)  # Connecting the find number button with the corresponding function
		self.ui.clear_btn.clicked.connect(self.clear)  # Linking the clear button with the corresponding function
		self.ui.checkBox.setChecked(True)
		self.ui.checkBox.toggled.connect(self.random_array)
		self.ui.checkBox_2.toggled.connect(self.array_yourself)
		self.ui.set_default_values.clicked.connect(self.set_default_array)
		self.ui.MplSort.canvas.axes.get_xaxis().set_visible(False)
		self.ui.MplSort.canvas.axes.get_yaxis().set_visible(False)
		self.ui.disp_unsorted_array.setReadOnly(True)
		self.ui.lower_range.setValidator(QIntValidator(-1000000, 10000, self))
		self.ui.upper_range.setValidator(QIntValidator(10000, 1000000, self))
		self.ui.mic_btn.clicked.connect(self.voice)

		self.ui.btn_close_3.clicked.connect(self.close)
		self.ui.btn_maximize_restore_3.clicked.connect(self.showMaximized)
		self.ui.btn_minimize_3.clicked.connect(self.showMinimized)

		self.setWindowFlags(Qt.CustomizeWindowHint)
		self.pressing = False

	def resizeEvent(self, QResizeEvent):
		super(BinarySearch, self).resizeEvent(QResizeEvent)
		self.ui.frame_top_binary.setFixedWidth(self.width())

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

	def voice(self):
		r = sr.Recognizer()
		microphoneValue = ""
		with sr.Microphone() as source:
			try:
				self.statusBar().showMessage('Start talking...')
				audio = r.listen(source)
				microphoneValue = (r.recognize_google(audio))
				self.statusBar().showMessage('Stop talking...')
				try:
					if microphoneValue == 'set default values':
						try:
							self.set_default_array()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")

					elif microphoneValue == 'create array':
						try:
							self.create_array()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")

					elif microphoneValue == 'sort':
						try:
							self.sortingarray()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")
					elif microphoneValue == 'find index':
						try:
							self.find_number()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")
					elif microphoneValue == 'clear':
						try:
							self.clear()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")
					elif microphoneValue == 'close':
						try:
							self.close()
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

	def set_default_array(self):
		self.lower = random.randint(-50, 0)
		self.ui.lower_range.setText(str(self.lower))
		self.upper = random.randint(50, 300)
		self.ui.upper_range.setText(str(self.upper))
		self.length = random.randint(10, 50)
		self.ui.display_arraylen.setText(str(self.length))
		self.ui.array_len.setValue(self.length)
		self.unsorted_array = binarySearch.createarray(self.lower, self.upper,
													   self.length)  # Calling the create array function from the project operations file
		self.unsorted_array = random.sample(self.unsorted_array, len(self.unsorted_array))
		self.t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
		self.ui.disp_unsorted_array.setText(str(self.unsorted_array))  # Display on the interface
		self.ui.MplSort.canvas.axes.clear()
		self.ui.MplSort.canvas.axes.set_title("Unsorted Array")
		self.rects = self.ui.MplSort.canvas.axes.bar(self.t, self.unsorted_array, color=(0.4, 0, 0.2), edgecolor="blue")
		self.autolabel(self.rects)
		self.ui.MplSort.canvas.axes.patch.set_alpha(0)
		self.ui.MplSort.canvas.draw()

	def random_array(self):
		self.ui.disp_unsorted_array.setReadOnly(True)
		self.ui.array_len.setEnabled(True)
		self.ui.checkBox_2.setChecked(False)
		self.ui.lower_range.setEnabled(True)
		self.ui.upper_range.setEnabled(True)
		self.ui.set_default_values.setEnabled(True)

	def array_yourself(self):
		self.ui.disp_unsorted_array.setReadOnly(False)
		self.ui.array_len.setEnabled(False)
		self.ui.checkBox.setChecked(False)
		self.ui.lower_range.setEnabled(False)
		self.ui.upper_range.setEnabled(False)
		self.ui.set_default_values.setEnabled(False)
		self.clear()

	def valuelen(self):  # Function of array size value taken from dial to show next to line edit
		self.length_array = self.ui.array_len.value()
		self.ui.display_arraylen.setText(str(self.length_array))

	# Function to write number values to a bar chart.
	def autolabel(self, rects):
		for rect in self.rects:
			height = rect.get_height()
			if height > 0:
				self.ui.MplSort.canvas.axes.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
												 '%d' % int(height), ha='center', va='bottom')
			else:
				self.ui.MplSort.canvas.axes.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
												 '%d' % int(height), ha='center', va='top')

	# %%Creating a random array and display it on the screen
	def create_array(self):
		if self.ui.checkBox.isChecked():  # function written to create an array
			try:
				try:
					self.lower = int(self.ui.lower_range.text())
					self.upper = int(self.ui.upper_range.text())
					if (self.lower != 0 and self.upper != 0) or self.length_array != 0:
						if self.lower < self.upper:
							if abs(self.upper - self.lower) > self.length_array:
								self.unsorted_array = binarySearch.createarray(self.lower, self.upper,
																			   self.length_array)  # Calling the create array function from the project operations file
								self.unsorted_array = random.sample(self.unsorted_array, len(self.unsorted_array))
								self.t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
								self.ui.disp_unsorted_array.setText(
									str(self.unsorted_array))  # Display on the interface
								self.ui.MplSort.canvas.axes.clear()
								self.ui.MplSort.canvas.axes.set_title("Unsorted Array")
								self.rects = self.ui.MplSort.canvas.axes.bar(self.t, self.unsorted_array,
																			 color=(0.4, 0, 0.2), edgecolor="blue")
								self.autolabel(self.rects)
								self.ui.MplSort.canvas.axes.patch.set_alpha(0)
								self.ui.MplSort.canvas.draw()
							else:
								self.msg = QMessageBox.critical(self, "Error",
																"Array length should be less than the difference between upper range and lower range.!")
						else:
							self.msg = QMessageBox.critical(self, "Error",
															"Upper range must be greater than lower range!")
					else:
						self.msg = QMessageBox.critical(self, "Error", "Please set the range and array size!")
				except ValueError:
					self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields!")
			except AttributeError:
				self.msg = QMessageBox.critical(self, "Error",
												"Please make the operations in order!")  # If the user presses another button without pressing this button, an error is given

		if self.ui.checkBox_2.isChecked():
			self.ui.disp_unsorted_array.setReadOnly(False)
			try:
				self.unsorted_array = self.ui.disp_unsorted_array.toPlainText().split(',')
				for i in range(len(self.unsorted_array)):
					self.unsorted_array[i] = int(self.unsorted_array[i])
				self.t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
				self.ui.disp_unsorted_array.setText(str(self.unsorted_array))  # Display on the interface
				self.ui.MplSort.canvas.axes.clear()
				self.ui.MplSort.canvas.axes.set_title("Unsorted Array")
				self.rects = self.ui.MplSort.canvas.axes.bar(self.t, self.unsorted_array, color=(0.4, 0, 0.2),
															 edgecolor="blue")
				self.autolabel(self.rects)
				self.ui.MplSort.canvas.axes.patch.set_alpha(0)
				self.ui.MplSort.canvas.draw()
			except ValueError:
				self.msg = QMessageBox.critical(self, "Error",
												"Please enter an array as valid format!")  # If the user presses another button without pressing this button, an error is given
				self.ui.disp_unsorted_array.clear()
				self.unsorted_array = []

	# %%Sorting a random array and display on the screen
	def sortingarray(self):
		try:
			if len(self.unsorted_array) != 0:
				self.sorted_array = binarySearch.insertionSort(
					self.unsorted_array)  # Calling the insertion sort function from the project operations file for sorting
				self.ui.disp_sorted_array.setText(str(self.sorted_array))  # Display on the interface
				self.ui.MplSort.canvas.axes.clear()
				self.ui.MplSort.canvas.axes.set_title("Sorted Array")
				self.rects = self.ui.MplSort.canvas.axes.bar(self.t, self.sorted_array, color=(0.4, 0, 0.2),
															 edgecolor="blue")
				self.autolabel(self.rects)
				self.ui.MplSort.canvas.axes.patch.set_alpha(0)
				self.ui.MplSort.canvas.draw()
			else:
				self.msg = QMessageBox.information(self, "Error", "Please create an array...")
		except AttributeError:
			self.msg = QMessageBox.critical(self, "Error",
											"Please make the operations in order!")  # If the user presses another button without pressing this button, an error is given
			self.ui.disp_sorted_array.clear()

	# %%Finding the index of the searched number and display on the screen
	def find_number(self):
		try:
			if len(self.sorted_array) != 0:
				self.number = int(self.ui.take_number.text())  # getting the desired number from the user
				if np.isin(self.number, self.sorted_array):  # Checking whether the desired number is in the array
					begin_index = 0
					end_index = len(self.sorted_array) - 1
					while True:
						midpoint = begin_index + (end_index - begin_index) // 2
						# if begin_index>end_index:
						#     self.ui.lineEdit_answer.setText("None")
						#     break

						if self.sorted_array[midpoint] == self.number:
							self.ui.MplSort.canvas.axes.clear()
							self.rects = self.ui.MplSort.canvas.axes.bar(self.t, self.sorted_array, color=(0.4, 0, 0.2),
																		 edgecolor=(0, .9, .9))
							self.autolabel(self.rects)
							self.ui.MplSort.canvas.axes.bar(self.t[midpoint], self.sorted_array[midpoint], color="red",
															edgecolor=(0, .9, .9))
							self.ui.MplSort.canvas.axes.patch.set_alpha(0)
							self.ui.MplSort.canvas.draw()
							self.ui.result_edit.setText("Element {} found at index '{}'.".format(str(self.number),
																								 str(midpoint + 1)))  # Display of result
							break

						else:

							self.ui.MplSort.canvas.axes.bar(self.t[midpoint], self.sorted_array[midpoint], color="blue",
															edgecolor=(0, .9, .9))
							self.ui.MplSort.canvas.axes.patch.set_alpha(0)
							self.ui.MplSort.canvas.draw()
							QApplication.processEvents()
							time.sleep(1)
						if self.sorted_array[midpoint] > self.number:
							end_index = midpoint - 1
						if self.sorted_array[midpoint] < self.number:
							begin_index = midpoint + 1
				else:
					self.msg3 = QMessageBox.information(self, "Error",
														"Please enter a sorted array elements...")  # give an error if the requested number is not in the array
					self.ui.MplSort.canvas.axes.clear()
					self.ui.MplSort.canvas.axes.set_title("Sorted Array")
					self.rects = self.ui.MplSort.canvas.axes.bar(self.t, self.sorted_array, color=(0.4, 0, 0.2),
																 edgecolor="black")
					self.autolabel(self.rects)
					self.ui.MplSort.canvas.axes.patch.set_alpha(0)
					self.ui.MplSort.canvas.draw()
					self.ui.take_number.clear()  # cleaning the section where the user entered numbers
					self.ui.result_edit.clear()
			else:
				self.msg = QMessageBox.critical(self, "Error", "Please make the operations in order!")
				self.ui.take_number.clear()
		except ValueError:
			self.msg = QMessageBox.information(self, "Error",
											   "Please enter a valid number...")  # error if user enters anything other than number
			self.ui.take_number.clear()  # cleaning the section where the user entered numbers
		except AttributeError:
			self.msg = QMessageBox.information(self, "Error", "Please create an array...")

	# %% Clear post-values with clear button
	def clear(self):
		self.lower = 0
		self.upper = 0
		self.length_array = 0
		self.unsorted_array = []
		self.sorted_array = []
		self.ui.MplSort.canvas.axes.clear()
		self.ui.MplSort.canvas.axes.patch.set_alpha(0)
		self.ui.MplSort.canvas.draw()
		self.ui.lower_range.clear()
		self.ui.upper_range.clear()
		self.ui.display_arraylen.clear()
		self.ui.disp_unsorted_array.clear()
		self.ui.disp_sorted_array.clear()
		self.ui.take_number.clear()
		self.ui.result_edit.clear()
		self.ui.array_len.setValue(0)


if __name__ == "__main__":
	app = QApplication([])
	window = BinarySearch()
	window.show()
	sys.exit(app.exec_())




