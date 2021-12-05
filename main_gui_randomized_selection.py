# Introduction to Algorithm course graphical interface design project randomized selection page.
# 5 December 2021.

# Written by Orhan Ozan Yildiz.
import random
import sys
import time

import numpy as np
import speech_recognition as sr
from PyQt5.QtGui import QIntValidator
# %% including required libraries, modules and files with code
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from uiqt_randomized_selection import Ui_RandomizedSelectionWindow
from utils_operations import randomized_selection

ran_sel = randomized_selection()


# %% Application Content
class RandomizedSelection(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_RandomizedSelectionWindow()  # Ability to use the class in which the interface I designed with qt designer converted into code
		self.ui.setupUi(self)
		self.ui.array_len.setMinimum(0)  # Fixing the dial to min 1 max 50
		self.ui.array_len.setMaximum(50)  # Link to print the number on the dial on the line edit next to it
		self.ui.array_len.valueChanged.connect(
			self.value_len)  # Link to print the number on the dial on the line edit next to it
		self.ui.createanarray_btn.clicked.connect(
			self.create_array)  # Connecting the create array button with the corresponding function
		self.ui.createanarray_btn.clicked.connect(self.sorting_array)
		self.ui.set_default_values.clicked.connect(self.set_default_array)
		self.ui.back_btn.clicked.connect(self.close)  # back to main menu
		self.ui.find_btn.clicked.connect(
			self.find_number)  # Connecting the find number button with the corresponding function
		self.ui.clear_btn.clicked.connect(self.clear)  # Linking the clear button with the corresponding function
		self.ui.random_array_checkbox.setChecked(True)
		self.ui.random_array_checkbox.toggled.connect(self.random_array)
		self.ui.create_array_checkbox.toggled.connect(self.array_yourself)
		self.ui.MplSort.canvas.axes.get_xaxis().set_visible(False)
		self.ui.MplSort.canvas.axes.get_yaxis().set_visible(False)
		self.ui.lower_range.setValidator(QIntValidator(-1000000, 10000, self))
		self.ui.upper_range.setValidator(QIntValidator(10000, 1000000, self))
		self.unsorted_array = []
		self.lower_range = 0
		self.upper_range = 0
		self.ui.mic_btn.clicked.connect(self.voice)

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

					elif microphoneValue == 'find':
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
		self.unsorted_array = ran_sel.createarray(self.lower, self.upper,
												  self.length)  # Calling the create array function from the project operations file
		self.unsorted_array = random.sample(self.unsorted_array, len(self.unsorted_array))
		self.sorting_array()
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
		self.ui.create_array_checkbox.setChecked(False)
		self.ui.lower_range.setEnabled(True)
		self.ui.upper_range.setEnabled(True)
		self.ui.set_default_values.setEnabled(True)

	def array_yourself(self):
		self.ui.disp_unsorted_array.setReadOnly(False)
		self.ui.array_len.setEnabled(False)
		self.ui.random_array_checkbox.setChecked(False)
		self.ui.lower_range.setEnabled(False)
		self.ui.upper_range.setEnabled(False)
		self.ui.set_default_values.setEnabled(False)
		self.clear()

	def value_len(self):  # Function of array size value taken from dial to show next to line edit
		self.length = self.ui.array_len.value()
		self.ui.display_arraylen.setText(str(self.length))

	def autolabel(self, rects):  # The function for writing number values ​​on the bar graph
		for rect in self.rects:
			height = rect.get_height()
			self.ui.MplSort.canvas.axes.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
											 '%d' % int(height),
											 ha='center', va='bottom')

	# %%#%%Creating a random array and display it on the screen
	def create_array(self):
		if self.ui.random_array_checkbox.isChecked():  # function written to create an array
			try:
				try:
					self.lower = int(self.ui.lower_range.text())
					self.upper = int(self.ui.upper_range.text())
					if (self.lower != 0 and self.upper != 0) or self.length != 0:
						if self.lower < self.upper:
							if abs(self.upper - self.lower) > self.length:
								self.unsorted_array = ran_sel.createarray(self.lower, self.upper,
																		  self.length)  # Calling the create array function from the project operations file
								self.unsorted_array = random.sample(self.unsorted_array, len(self.unsorted_array))
								self.t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
								self.ui.disp_unsorted_array.setText(
									str(self.unsorted_array))  # Display on the interface
								self.ui.MplSort.canvas.axes.clear()
								self.ui.MplSort.canvas.axes.set_title("Unsorted Array")
								self.rects = self.ui.MplSort.canvas.axes.bar(self.t, self.unsorted_array,
																			 color='orange', edgecolor="blue")
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

		if self.ui.create_array_checkbox.isChecked():
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
	def sorting_array(self):
		if len(self.unsorted_array) != 0:
			temp_array1 = tuple(self.unsorted_array)
			temp_array1 = list(temp_array1)
			self.sorted_array = ran_sel.insertionSort(
				temp_array1)  # Calling the insertion sort function from the project operations file for sorting
			self.ui.disp_sorted_array.setText(str(self.sorted_array))  # Display on the interface
		# self.t = np.lin-space(1, len(self.unsorted_array), len(self.unsorted_array))
		# self.ui.MplSort.canvas.axes.clear()
		# self.ui.MplSort.canvas.axes.set_title("Sorted Array")
		# self.rects=self.ui.MplSort.canvas.axes.bar(self.t, self.sorted_array, color="orange", edge color="black")
		# self.autolabel(self.rects)
		# self.ui.MplSort.canvas.draw()
		else:
			pass

	# %%Finding the index of the searched number and display on the screen
	def find_number(self):
		try:
			if len(self.sorted_array) != 0:
				self.number = int(self.ui.take_number.text())  # getting the desired number from the user
				if self.number <= len(self.unsorted_array):  # Checking whether the desired number is in the array
					self.smallest = self.randomized_select(self.unsorted_array, 0, len(self.sorted_array) - 1,
														   self.number)  # Calling the binary search function from the project operations file for search
					self.ui.result_edit.setText(
						"{}. smallest array is '{}'.".format(str(self.number), str(self.smallest)))  # Display of result

				else:
					self.msg3 = QMessageBox.information(self, "Error",
														"Please enter a sorted array elements...")  # give an error if the requested number is not in the array
					self.ui.take_number.clear()  # cleaning the section where the user entered numbers
					self.ui.result_edit.clear()
			else:
				self.msg = QMessageBox.critical(self, "Error", "Please make the operations in order!")
		except ValueError:
			self.msg = QMessageBox.information(self, "Error",
											   "Please enter a valid number...")  # error if user enters anything other than number
			self.ui.take_number.clear()  # cleaning the section where the user entered numbers
		except AttributeError:
			self.msg = QMessageBox.information(self, "Error", "Please create an array...")

	# %%

	def partition(self, array, p, r):
		x = array[r]
		i = p - 1
		for j in range(p, r):
			if array[j] <= x:
				i += 1
				array[i], array[j] = array[j], array[i]
		array[i + 1], array[r] = array[r], array[i + 1]
		self.x = np.arange(len(array))
		self.ui.MplSort.canvas.axes.clear()
		self.rects = self.ui.MplSort.canvas.axes.bar(self.x, array, color="orange", edgecolor="black")
		self.ui.MplSort.canvas.axes.bar(self.x[r], array[r], color="green", edgecolor='black')
		self.ui.MplSort.canvas.axes.bar(self.x[i], array[i], color="purple", edgecolor='black')
		self.autolabel(self.rects)
		self.ui.MplSort.canvas.axes.patch.set_alpha(0)
		self.ui.MplSort.canvas.draw()
		QApplication.processEvents()
		time.sleep(1)
		return (i + 1)

	def randomized_partition(self, array, p, r):
		i = random.randint(p, r)
		self.x = np.arange(len(array))
		self.ui.MplSort.canvas.axes.clear()
		self.rects = self.ui.MplSort.canvas.axes.bar(self.x, array, color=(0, 0, 0, 0.1), edgecolor='blue')
		self.autolabel(self.rects)
		self.ui.MplSort.canvas.draw()
		array[r], array[i] = array[i], array[r]
		return self.partition(array, p, r)

	def randomized_select(self, array, p, q, i):
		if p == q:
			self.ui.MplSort.canvas.axes.clear()
			self.rects = self.ui.MplSort.canvas.axes.bar(self.x, array, color="orange", edgecolor="black")
			self.ui.MplSort.canvas.axes.bar(self.x[p], array[q], color="blue", edgecolor='blue')
			self.autolabel(self.rects)
			self.ui.MplSort.canvas.axes.patch.set_alpha(0)
			self.ui.MplSort.canvas.draw()
			return array[p]
		r = self.randomized_partition(array, p, q)
		k = r - p + 1
		if i == k:
			self.ui.MplSort.canvas.axes.clear()
			self.rects = self.ui.MplSort.canvas.axes.bar(self.x, array, color="orange", edgecolor="black")
			self.ui.MplSort.canvas.axes.bar(self.x[r], array[r], color="blue", edgecolor='blue')
			self.autolabel(self.rects)
			self.ui.MplSort.canvas.axes.patch.set_alpha(0)
			self.ui.MplSort.canvas.draw()
			return array[r]
		elif i < k:
			return self.randomized_select(array, p, r - 1, i)
		else:
			return self.randomized_select(array, r + 1, q, i - k)

	# %% Clear post-values with clear button
	def clear(self):
		self.lower = 0
		self.upper = 0
		self.length = 0
		self.unsorted_array = []
		self.sorted_array = []
		self.ui.lower_range.clear()
		self.ui.upper_range.clear()
		self.ui.display_arraylen.clear()
		self.ui.disp_unsorted_array.clear()
		self.ui.disp_sorted_array.clear()
		self.ui.take_number.clear()
		self.ui.result_edit.clear()
		self.ui.MplSort.canvas.axes.clear()
		self.ui.MplSort.canvas.axes.patch.set_alpha(0)
		self.ui.MplSort.canvas.draw()
		self.ui.array_len.setValue(0)


if __name__ == "__main__":
	app = QApplication([])
	window = RandomizedSelection()
	window.show()
	sys.exit(app.exec_())
