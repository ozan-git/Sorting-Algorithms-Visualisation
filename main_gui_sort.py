# Introduction to Algorithm course graphical interface design project sort page.
# 5 December 2021.

# Written by Orhan Ozan Yildiz.
import csv
import random
import sys
import time
import tkinter as tk
from tkinter import filedialog

import numpy as np
import pandas as pd
import speech_recognition as sr
import xlsxwriter
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
# %% including required libraries, modules and files with code
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog

from main_gui_input_array import ArrayWindow
from main_gui_time_comparison import TimeComparisonMainWindow
from uiqt_sorting import Ui_SortWindow
from utils_operations import binarysearch

binarySearch = binarysearch()


# %%
class SortingAlgorithms(QMainWindow):
	stop_array = "global"

	def __init__(self):
		super().__init__()
		self.ui = Ui_SortWindow()
		self.ui.setupUi(self)
		self.setWindowTitle('Sorting Algorithms Visualisations')
		self.AddArray = ArrayWindow()
		self.time_comp = TimeComparisonMainWindow()
		self.ui.array_sort.setMinimum(0)
		self.ui.array_sort.setMaximum(100)
		self.ui.lower_range.setValidator(QIntValidator(-1000000, 10000, self))
		self.ui.upper_range.setValidator(QIntValidator(10000, 1000000, self))
		self.ui.array_sort.valueChanged.connect(self.valuelen)
		self.ui.set_default_values.clicked.connect(self.SetDefaultValues)
		self.ui.set_default_values.clicked.connect(self.spin_box)
		self.ui.set_default_values.clicked.connect(self.createbargraph)
		self.ui.create_array.clicked.connect(self.CreateArray)
		self.ui.create_array.clicked.connect(self.spin_box)
		self.ui.enter_array.clicked.connect(self.add_array)
		self.ui.stop_btn.clicked.connect(self.stop_button)
		self.ui.skip_btn.clicked.connect(self.skip_button)
		self.ui.time_comparison.clicked.connect(self.time_comparison_open)
		self.ui.MplSort.canvas.axes.get_xaxis().set_visible(False)
		self.ui.MplSort.canvas.axes.get_yaxis().set_visible(False)

		self.AddArray.array_signal.connect(self.add_array)
		self.AddArray.array_signal.connect(self.take_user_array)
		self.unsorted_array = []

		self.ui.micro_btn.clicked.connect(self.voice)

		self.ui.menuSave_File.triggered.connect(self.save_response)
		self.ui.menuInsert_File.triggered.connect(self.insert_response)

		self.ui.create_array.clicked.connect(self.createbargraph)
		self.ui.clear_btn.clicked.connect(self.clear)
		self.ui.back_btn.clicked.connect(self.close)
		self.ui.verticalSlider.setFocusPolicy(Qt.NoFocus)
		self.ui.MplSort.canvas.axes.get_xaxis().set_visible(False)
		self.ui.bubble_sort.clicked.connect(self.BubbleSort)
		self.ui.insertion_sort.clicked.connect(self.InsertionSort)
		self.ui.merge_sort.clicked.connect(self.callmerge)
		self.ui.selection_sort.clicked.connect(self.SelectionSort)
		self.ui.quick_sort.clicked.connect(self.callquicksort)
		self.ui.heap_sort.clicked.connect(self.HeapSort)
		self.ui.counting_sort.clicked.connect(self.CountingSort)
		self.ui.bucket_sort.clicked.connect(self.BucketSort)
		self.ui.shell_sort.clicked.connect(self.ShellSort)
		self.ui.radix_sort.clicked.connect(self.RadixSort)
		self.ui.coctail_sort.clicked.connect(self.CoctailSort)
		self.ui.comb_sort.clicked.connect(self.callcombsort)

		self.ui.pushButton.clicked.connect(self.plus)
		self.ui.pushButton_2.clicked.connect(self.minus)

	def spin_box(self):
		self.seed_value = self.ui.spinBox.value()

	def plus(self):
		temp_min = self.ui.array_sort.minimum()
		temp_max = self.ui.array_sort.maximum()
		self.ui.array_sort.setMinimum(temp_min + 100)
		self.ui.array_sort.setMaximum(temp_max + 100)

	def minus(self):
		temp_min = self.ui.array_sort.minimum()
		temp_max = self.ui.array_sort.maximum()
		if temp_min > 0:
			self.ui.array_sort.setMinimum(temp_min - 100)
			self.ui.array_sort.setMaximum(temp_max - 100)
		else:
			QMessageBox.warning(self, "ERROR", "The range you set for the array length must be at least 0!")

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
					if microphoneValue == 'bubble sort':
						try:
							self.BubbleSort()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Create array first...")
					elif microphoneValue == 'insertion sort':
						try:
							self.InsertionSort()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Create array first...")
					elif microphoneValue == 'merge sort':
						try:
							self.callmerge()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Create array first...")
					elif microphoneValue == 'heap sort':
						try:
							self.HeapSort()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Create array first...")
					elif microphoneValue == 'selection sort':
						try:
							self.SelectionSort()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Create array first...")
					elif microphoneValue == 'quicksort':
						try:
							self.callquicksort()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Create array first...")
					elif microphoneValue == 'bucket sort':
						try:
							self.BucketSort()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Create array first...")
					elif microphoneValue == 'counting sort':
						try:
							self.CountingSort()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Create array first...")
					elif microphoneValue == 'radix sort':
						try:
							self.RadixSort()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Create array first...")
					elif microphoneValue == 'shell sort':
						try:
							self.ShellSort()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Create array first...")
					elif microphoneValue == 'default':
						try:
							self.SetDefaultValues()
							self.createbargraph()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Create array first...")
					elif microphoneValue == 'insert array':
						try:
							self.add_array()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Create array first...")
					elif microphoneValue == 'clear':
						try:
							self.clear()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Create array first...")
					elif microphoneValue == 'time comparison':
						try:
							self.time_comparison_open()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Create array first...")
					elif microphoneValue == 'close':
						try:
							self.close()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Create array first...")
					elif microphoneValue == 'coctail sort':
						try:
							self.CoctailSort()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Create array first...")
					elif microphoneValue == 'comb sort':
						try:
							self.callcombsort()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Create array first...")
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

	# %%Save Array Operations
	def save_response(self, action):
		if action.text() == "Txt File":
			if len(self.unsorted_array) != 0:
				try:
					root = tk.Tk()
					root.withdraw()
					filepath = filedialog.asksaveasfilename(
						defaultextension="txt",
						filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
					)
					with open(filepath, "w") as output_file:
						text = str(self.unsorted_array)
						text = text.strip("[")
						text = text.strip("]")
						output_file.write(text)
				except FileNotFoundError:
					self.msg = QMessageBox.critical(self, "Error", "Array could not save...")
			else:
				self.msg = QMessageBox.critical(self, "Error", "Please create an array...")

		elif action.text() == "Csv File":
			if len(self.unsorted_array) != 0:
				try:
					root = tk.Tk()
					root.withdraw()
					filepath = filedialog.asksaveasfilename(
						defaultextension="csv",
						filetypes=[("csv file", "*.csv"), ("All Files", "*.*")],
					)

					with open(filepath, "w") as output_file:
						text = str(self.unsorted_array)
						text = text.strip("[")
						text = text.strip("]")
						output_file.write(text)
				except FileNotFoundError:
					self.msg = QMessageBox.critical(self, "Error", "Array could not save...")
			else:
				self.msg = QMessageBox.critical(self, "Error", "Please create an array...")

		elif action.text() == "Xlsx File":
			if len(self.unsorted_array) != 0:
				try:
					save_file = QFileDialog.getSaveFileName(self, "Select the excel file to save", "", "*.xlsx")
					self.excel_file = xlsxwriter.Workbook(save_file[0])
					self.save = self.excel_file.add_worksheet()
					row = 0
					column = 0
					for i in range(len(self.unsorted_array)):
						self.save.write(row, column, self.unsorted_array[i])
						column += 1
					self.excel_file.close()
				except FileNotFoundError:
					self.msg = QMessageBox.critical(self, "Error", "Array could not save...")
			else:
				self.msg = QMessageBox.critical(self, "Error", "Please create an array...")

	# %%Insert Array Operations
	def insert_response(self, action):
		if action.text() == "Txt File":
			try:
				root = tk.Tk()
				root.withdraw()
				file_path = filedialog.askopenfilename(initialdir="/", title="Select file",
													   filetypes=(("text file", "*.txt"), ("all files", "*.*")))
				text_file = open(file_path, "r")
				self.unsorted_array = text_file.read().split(',')
				for i in range(len(self.unsorted_array)):
					self.unsorted_array[i] = int(self.unsorted_array[i])
				t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
				self.ui.MplSort.canvas.axes.clear()
				self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#4dffff', edgecolor="black")
				self.autolabel(self.rects)
				self.ui.MplSort.canvas.axes.patch.set_alpha(0)
				self.ui.MplSort.canvas.draw()
			except ValueError:
				self.msg = QMessageBox.critical(self, "Error", "Please check your file...")
			except FileNotFoundError:
				self.msg = QMessageBox.critical(self, "Error", "Please choose a file...")
		elif action.text() == "Csv File":
			try:
				root = tk.Tk()
				root.withdraw()
				file_path = filedialog.askopenfilename(initialdir="/", title="Select file",
													   filetypes=(("csv file", "*.csv"), ("all files", "*.*")))
				with open(file_path) as f:
					okur = csv.reader(f)
					for satır in okur:
						self.unsorted_array = satır
					for i in range(len(self.unsorted_array)):
						self.unsorted_array[i] = int(self.unsorted_array[i])
					t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
					self.ui.MplSort.canvas.axes.clear()
					self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#4dffff',
																 edgecolor="black")
					self.autolabel(self.rects)
					self.ui.MplSort.canvas.axes.patch.set_alpha(0)
					self.ui.MplSort.canvas.draw()
			except ValueError:
				self.msg = QMessageBox.critical(self, "Error", "Please check your file...")
			except FileNotFoundError:
				self.msg = QMessageBox.critical(self, "Error", "Please choose a file...")
		elif action.text() == "Xlsx File":
			try:
				root = tk.Tk()
				root.withdraw()
				file_path = filedialog.askopenfilename(initialdir="/", title="Select file",
													   filetypes=(("xlsx file", "*.xlsx"), ("all files", "*.*")))
				df = pd.read_excel(file_path)
				self.unsorted_array = df.columns
				self.unsorted_array = list(self.unsorted_array)
				print(self.unsorted_array)
				for i in range(len(self.unsorted_array)):
					self.unsorted_array[i] = int(self.unsorted_array[i])
				t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
				self.ui.MplSort.canvas.axes.clear()
				self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#4dffff', edgecolor="black")
				self.autolabel(self.rects)
				self.ui.MplSort.canvas.axes.patch.set_alpha(0)
				self.ui.MplSort.canvas.draw()
			except ValueError:
				self.msg = QMessageBox.critical(self, "Error", "Please check your file...")
			except FileNotFoundError:
				self.msg = QMessageBox.critical(self, "Error", "Please choose a file...")

	# %%Stop Button
	def stop_button(self):
		if self.ui.stop_btn.text() == "Stop":
			self.ui.stop_btn.setText("Continue")
			self.ui.stop_btn.setStyleSheet("font: 10pt \"MS Shell Dlg 2\" white;\n"
										   "border-radius: 10px ;\n"
										   "background-color: rgb(0, 0, 0);\n"
										   "color: white;")
			global stop_array
			self.stop_array = int(1)
		elif self.ui.stop_btn.text() == "Continue":
			self.ui.stop_btn.setText("Stop")
			self.ui.stop_btn.setStyleSheet("font: 10pt \"MS Shell Dlg 2\" white;\n"
										   "border-radius: 10px ;\n"
										   "background-color: rgb(0, 0, 0);\n"
										   "color: white;")
			global stop_array
			self.stop_array = int(0)

	# %%Stop Button
	def skip_button(self):
		global stop_array
		global unsorted_array
		self.ui.MplSort.canvas.axes.clear()
		self.stop_array = int(2)
		if self.stop_array == 2:
			sorted_array = self.unsorted_array
			sorted_array.sort()
			t = np.arange(len(sorted_array))
			self.ui.MplSort.canvas.axes.clear()
			self.rects = self.ui.MplSort.canvas.axes.bar(t, sorted_array, color="green")
			self.autolabel(self.rects)
			self.ui.MplSort.canvas.draw()

	def operation_buttons(self):
		global stop_array
		global unsorted_array
		while self.stop_array == 1:
			if self.stop_array == 0:
				if self.stop_array == 2:
					self.ui.MplSort.canvas.axes.clear()
					break
				break
			time.sleep(1)
			QtCore.QCoreApplication.processEvents()
			if self.stop_array == 2:
				self.ui.MplSort.canvas.axes.clear()
				break

	# %% Time Comparison Window
	def time_comparison_open(self):
		self.time_comp.clear()
		self.time_comp.show()

	# %%Enter array by user
	def add_array(self):
		self.AddArray.clear()
		self.AddArray.show()
		self.ui.MplSort.canvas.axes.clear()
		self.ui.MplSort.canvas.axes.patch.set_alpha(0)
		self.ui.MplSort.canvas.draw()

	def take_user_array(self, array):
		self.unsorted_array = array
		t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
		self.ui.MplSort.canvas.axes.clear()
		self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#4dffff', edgecolor="black")
		self.autolabel(self.rects)
		self.ui.MplSort.canvas.axes.patch.set_alpha(0)
		self.ui.MplSort.canvas.draw()

	# %% Disable and Enable Buttons
	def disable_button(self):
		self.ui.create_array.setEnabled(False)
		self.ui.back_btn.setEnabled(False)
		self.ui.bubble_sort.setEnabled(False)
		self.ui.insertion_sort.setEnabled(False)
		self.ui.merge_sort.setEnabled(False)
		self.ui.selection_sort.setEnabled(False)
		self.ui.quick_sort.setEnabled(False)
		self.ui.heap_sort.setEnabled(False)
		self.ui.counting_sort.setEnabled(False)
		self.ui.bucket_sort.setEnabled(False)
		self.ui.shell_sort.setEnabled(False)
		self.ui.radix_sort.setEnabled(False)
		self.ui.set_default_values.setEnabled(False)
		self.ui.comb_sort.setEnabled(False)
		self.ui.coctail_sort.setEnabled(False)
		self.ui.time_comparison.setEnabled(False)
		self.ui.micro_btn.setEnabled(False)

	def enable_button(self):
		self.ui.create_array.setEnabled(True)
		self.ui.back_btn.setEnabled(True)
		self.ui.bubble_sort.setEnabled(True)
		self.ui.insertion_sort.setEnabled(True)
		self.ui.merge_sort.setEnabled(True)
		self.ui.selection_sort.setEnabled(True)
		self.ui.quick_sort.setEnabled(True)
		self.ui.heap_sort.setEnabled(True)
		self.ui.counting_sort.setEnabled(True)
		self.ui.bucket_sort.setEnabled(True)
		self.ui.shell_sort.setEnabled(True)
		self.ui.radix_sort.setEnabled(True)
		self.ui.set_default_values.setEnabled(True)
		self.ui.comb_sort.setEnabled(True)
		self.ui.coctail_sort.setEnabled(True)
		self.ui.time_comparison.setEnabled(True)
		self.ui.micro_btn.setEnabled(True)

	# %% Change in Dial
	def valuelen(self):
		self.length = int(self.ui.array_sort.value())
		self.ui.displayarrays_sort.setText(str(self.length))

	# %% Set the speed
	def projectspeed(self):
		self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())

	# %%Create Array with selected values and options
	def CreateArray(self):
		self.unsorted_array = []
		try:
			try:
				self.lower = int(self.ui.lower_range.text())
				self.upper = int(self.ui.upper_range.text())
				if (self.lower == 0 and self.upper == 0) or self.length == 0:
					self.msg = QMessageBox.critical(self, "Error",
													"Fill in the required fields...!\nMake sure to set to Array Size and Range...")
				else:
					if self.lower > self.upper:
						self.msg = QMessageBox.critical(self, "Error",
														'Upper range must be greater than lower range...')
						self.clear()
					else:
						if self.ui.checkBox.isChecked():
							random.seed(self.seed_value)
							random.sample
							if self.ui.checkBox_2.isChecked():
								if abs(self.upper - self.lower) < self.length:
									self.msg = QMessageBox.critical(self, "Error",
																	"'The length value cannot bigger than the difference on the lower and upper limit must be bigger than the length value.")
									self.clear()
								else:
									self.unsorted_array = []
									while len(self.unsorted_array) < self.length:
										x = random.randint(self.lower, self.upper)
										if not np.isin(x, self.unsorted_array):
											self.unsorted_array.append(x)

							else:
								self.unsorted_array = []
								while True:
									self.unsorted_array.append(random.randint(self.lower, self.upper))
									if len(self.unsorted_array) == self.length:
										break
						else:
							if self.ui.checkBox_2.isChecked():
								if abs(self.upper - self.lower) < self.length:
									self.msg = QMessageBox.critical(self, "Error",
																	"'The length value cannot bigger than the difference on the lower and upper limit must be bigger than the length value.")
									self.clear()
								else:
									self.unsorted_array = []
									while len(self.unsorted_array) < self.length:
										x = random.randint(self.lower, self.upper)
										if not np.isin(x, self.unsorted_array):
											self.unsorted_array.append(x)

							else:
								self.unsorted_array = []
								while True:
									self.unsorted_array.append(random.randint(self.lower, self.upper))
									if len(self.unsorted_array) == self.length:
										break
			except ValueError:
				self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields!")
		except AttributeError:
			self.msg = QMessageBox.critical(self, "Error", "Please make the operations in order!")

	# %%Default Random Array
	def SetDefaultValues(self):
		self.lower = random.randint(-50, 0)
		self.ui.lower_range.setText(str(self.lower))
		self.upper = random.randint(50, 300)
		self.ui.upper_range.setText(str(self.upper))
		self.length = random.randint(10, 50)
		self.ui.displayarrays_sort.setText(str(self.length))
		if self.ui.checkBox.isChecked():
			random.seed(self.seed_value)
			random.sample
			if self.ui.checkBox_2.isChecked():
				self.unsorted_array = []
				while len(self.unsorted_array) < self.length:
					x = random.randint(self.lower, self.upper)
					if not np.isin(x, self.unsorted_array):
						self.unsorted_array.append(x)

			else:
				self.unsorted_array = []
				while True:
					self.unsorted_array.append(random.randint(self.lower, self.upper))
					if len(self.unsorted_array) == self.length:
						break
		else:
			if self.ui.checkBox_2.isChecked():
				self.unsorted_array = []
				while len(self.unsorted_array) < self.length:
					x = random.randint(self.lower, self.upper)
					if not np.isin(x, self.unsorted_array):
						self.unsorted_array.append(x)

			else:
				self.unsorted_array = []
				while True:
					self.unsorted_array.append(random.randint(self.lower, self.upper))
					if len(self.unsorted_array) == self.length:
						break

	# %%Bar Graph Function
	def createbargraph(self):
		t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
		self.ui.MplSort.canvas.axes.clear()
		self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#4dffff', edgecolor="black")
		self.autolabel(self.rects)
		self.ui.MplSort.canvas.axes.patch.set_alpha(0)
		self.ui.MplSort.canvas.draw()

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

	# %%Bubble Sort Animation
	def BubbleSort(self):
		try:
			if len(self.unsorted_array) == 0:
				self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
			else:
				self.disable_button()
				t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
				for i in range(0, len(self.unsorted_array) - 1):  # loop for all array elements
					for j in range(0, len(self.unsorted_array) - i - 1):  # second cycle for swap operations
						if self.unsorted_array[j + 1] < self.unsorted_array[j]:  # if the left greater than right
							self.operation_buttons()
							self.ui.MplSort.canvas.axes.clear()
							self.ui.MplSort.canvas.axes.set_title("Bubble Sort Animation", loc='left')
							self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
																		 edgecolor="#f0f8ff")
							self.autolabel(self.rects)
							self.rects = self.ui.MplSort.canvas.axes.bar(t[j], self.unsorted_array[j], color="#FFE4E1",
																		 edgecolor="black")
							self.autolabel(self.rects)
							self.ui.MplSort.canvas.axes.bar(t[j + 1], self.unsorted_array[j + 1], color="#FFE4E1",
															edgecolor="black")
							self.autolabel(self.rects)
							self.ui.MplSort.canvas.axes.patch.set_alpha(0)
							self.ui.MplSort.canvas.draw()
							self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
							time.sleep(self.speedofproject)
							QApplication.processEvents()

							self.unsorted_array[j], self.unsorted_array[j + 1] = self.unsorted_array[j + 1], \
																				 self.unsorted_array[j]

							self.ui.MplSort.canvas.axes.clear()
							self.ui.MplSort.canvas.axes.set_title("Bubble Sort Animation", loc='left')
							self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
																		 edgecolor="#f0f8ff")
							self.autolabel(self.rects)
							self.rects = self.ui.MplSort.canvas.axes.bar(t[j], self.unsorted_array[j], color="#FFE4E1",
																		 edgecolor="black")
							self.autolabel(self.rects)
							self.rects = self.ui.MplSort.canvas.axes.bar(t[j + 1], self.unsorted_array[j + 1],
																		 color="#FFE4E1", edgecolor="black")
							self.autolabel(self.rects)
							self.ui.MplSort.canvas.axes.patch.set_alpha(0)
							self.ui.MplSort.canvas.draw()
							self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
							time.sleep(self.speedofproject)
							QApplication.processEvents()
				self.ui.MplSort.canvas.axes.clear()
				self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
															 edgecolor="#f0f8ff")
				self.autolabel(self.rects)
				self.ui.MplSort.canvas.axes.patch.set_alpha(0)
				self.ui.MplSort.canvas.draw()
				self.enable_button()
		except AttributeError:
			self.msg = QMessageBox.critical(self, "Error",
											"Fill in the required fields...!\nMake sure to set to Array Size and Range...")
			self.enable_button()

	# %%Insertion Sort Animation
	def InsertionSort(self):
		try:
			if len(self.unsorted_array) == 0:
				self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
			else:
				self.disable_button()
				t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
				for i in range(1, len(self.unsorted_array)):
					j = i - 1
					key = self.unsorted_array[i]
					while (self.unsorted_array[j] > key) and (j >= 0):
						self.unsorted_array[j + 1] = self.unsorted_array[j]
						j -= 1
						self.operation_buttons()
						self.ui.MplSort.canvas.axes.clear()
						self.ui.MplSort.canvas.axes.set_title("Insertion Sort Animation", loc='left')
						self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
																	 edgecolor="#f0f8ff")
						self.autolabel(self.rects)
						self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="#FFE4E1",
																	 edgecolor="black")
						self.autolabel(self.rects)
						self.rects = self.ui.MplSort.canvas.axes.bar(t[j + 1], self.unsorted_array[j + 1],
																	 color="#FFE4E1", edgecolor="black")
						self.autolabel(self.rects)
						self.ui.MplSort.canvas.axes.patch.set_alpha(0)
						self.ui.MplSort.canvas.draw()
						self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
						time.sleep(self.speedofproject)
						QApplication.processEvents()

					self.unsorted_array[j + 1] = key
					self.ui.MplSort.canvas.axes.clear()
					self.ui.MplSort.canvas.axes.set_title("Insertion Sort Animation", loc='left')
					self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
																 edgecolor="#f0f8ff")
					self.autolabel(self.rects)
					self.ui.MplSort.canvas.axes.patch.set_alpha(0)
					self.ui.MplSort.canvas.draw()
					self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
					time.sleep(self.speedofproject)
					QApplication.processEvents()
				self.enable_button()

		except AttributeError:
			self.msg = QMessageBox.critical(self, "Error",
											"Please make the operations in order!\nMake sure to set to Array Size and Range")
			self.enable_button()

	# %% Merge Sort Animation
	def callmerge(self):
		try:
			if len(self.unsorted_array) == 0:
				self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
			else:
				self.disable_button()
				array = self.unsorted_array
				self.MergeSort(array, 0, len(self.unsorted_array) - 1)
				self.enable_button()
		except AttributeError:
			self.msg = QMessageBox.critical(self, "Error",
											"Please make the operations in order!\nMake sure to set to Array Size and Range")
			self.enable_button()

	def MergeSort(self, array, p, r):
		if p < r:  # p is the first index, r is the last index.
			q = (p + r) // 2  # q is the middle index
			self.MergeSort(array, p, q)  # recursive function for new right array created
			self.MergeSort(array, q + 1, r)  # recursive function for new right array created
			self.merge(array, p, q, r)  # merge funciton for sorted array to merge
		return array

	def merge(self, array, p, q, r):
		t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
		n1 = q - p + 1  # left array of length is n1
		n2 = r - q  # right array of length is n2
		left_array = np.empty(n1 + 1)  # computes the length n1+1 of the subarray
		right_array = np.empty(n2 + 1)  # computes the length n2+1 of the subarray
		for i in range(n1):  # The for loop of copies the subarray divided array into left array
			left_array[i] = array[p + i]
		for j in range(n2):  # The for loop of copies the subarray divided array into right array
			right_array[j] = array[q + 1 + j]
		left_array[n1] = np.inf  # use inf value as the sentinel value
		right_array[n2] = np.inf  # use inf value as the sentinel value

		i = 0  # empty subarray contains the 0 smallest elements of left array and right array
		j = 0
		for k in range(p, r + 1):  # the subarrays indexes compare
			if left_array[i] <= right_array[
				j]:  # campare left array ith index and right array jth index for sorted array
				array[k] = left_array[i]  # the smaller one is added to the arrays about to be sorted
				i += 1
				self.operation_buttons()
				self.ui.MplSort.canvas.axes.clear()
				self.ui.MplSort.canvas.axes.set_title("Merge Sort Animation", loc='left')
				self.rects = self.ui.MplSort.canvas.axes.bar(t, array, color='#56132a', edgecolor="#f0f8ff")
				self.autolabel(self.rects)
				self.rects = self.ui.MplSort.canvas.axes.bar(t[k], array[k], color="gray", edgecolor="black")
				self.autolabel(self.rects)
				self.rects = self.ui.MplSort.canvas.axes.bar(t[i - 1], array[i - 1], color="red", edgecolor="black")
				self.autolabel(self.rects)
				# self.ui.MplSort.canvas.axes.bar(t[i+1], array[i+1], color="blue", edgecolor="black")
				self.ui.MplSort.canvas.axes.patch.set_alpha(0)
				self.ui.MplSort.canvas.draw()
				self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
				time.sleep(self.speedofproject)
				QApplication.processEvents()
			else:
				array[k] = right_array[j]
				j += 1
				self.ui.MplSort.canvas.axes.clear()
				self.ui.MplSort.canvas.axes.set_title("Merge Sort Animation", loc='left')
				self.rects = self.ui.MplSort.canvas.axes.bar(t, array, color='#56132a', edgecolor="#f0f8ff")
				self.autolabel(self.rects)
				self.rects = self.ui.MplSort.canvas.axes.bar(t[k], array[k], color="gray", edgecolor="black")
				self.autolabel(self.rects)
				self.rects = self.ui.MplSort.canvas.axes.bar(t[j - 1], array[j - 1], color="red", edgecolor="black")
				self.autolabel(self.rects)
				# self.ui.MplSort.canvas.axes.bar(t[j+1], array[j+1], color="blue", edgecolor="black")
				self.ui.MplSort.canvas.axes.patch.set_alpha(0)
				self.ui.MplSort.canvas.draw()
				self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
				time.sleep(self.speedofproject)
				QApplication.processEvents()

		self.ui.MplSort.canvas.axes.clear()
		self.ui.MplSort.canvas.axes.set_title("Merge Sort Animation", loc='left')
		self.rects = self.ui.MplSort.canvas.axes.bar(t, array, color='#56132a', edgecolor="#f0f8ff")
		self.ui.MplSort.canvas.axes.patch.set_alpha(0)
		self.autolabel(self.rects)
		self.ui.MplSort.canvas.draw()

	# %% Selection Sort Animation
	def SelectionSort(self):
		try:
			if len(self.unsorted_array) == 0:
				self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
			else:
				self.disable_button()
				t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
				for i in range(len(self.unsorted_array)):
					min = i
					for j in range(i + 1, len(self.unsorted_array)):
						if self.unsorted_array[min] > self.unsorted_array[j]:
							min = j

							self.ui.MplSort.canvas.axes.clear()
							self.ui.MplSort.canvas.axes.set_title("Selection Sort Animation", loc='left')
							self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
																		 edgecolor="#f0f8ff")
							self.autolabel(self.rects)
							self.rects = self.ui.MplSort.canvas.axes.bar(t[j], self.unsorted_array[j], color="blue",
																		 edgecolor="black")
							self.autolabel(self.rects)
							self.rects = self.ui.MplSort.canvas.axes.bar(t[min], self.unsorted_array[min], color="red",
																		 edgecolor="white")
							self.autolabel(self.rects)
							self.ui.MplSort.canvas.axes.patch.set_alpha(0)
							self.ui.MplSort.canvas.draw()
							self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
							time.sleep(self.speedofproject)
							QApplication.processEvents()
					self.operation_buttons()
					self.unsorted_array[i], self.unsorted_array[min] = self.unsorted_array[min], self.unsorted_array[i]

				self.ui.MplSort.canvas.axes.clear()
				self.ui.MplSort.canvas.axes.set_title("Selection Sort Animation", loc='left')
				self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
															 edgecolor="#f0f8ff")
				self.autolabel(self.rects)
				self.ui.MplSort.canvas.axes.patch.set_alpha(0)
				self.ui.MplSort.canvas.draw()
				self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
				time.sleep(self.speedofproject)
				QApplication.processEvents()
				self.enable_button()
		except AttributeError:
			self.msg = QMessageBox.critical(self, "Error",
											"Please make the operations in order!\nMake sure to set to Array Size and Range")
			self.enable_button()

	# %% Quick Sort Animation
	def callquicksort(self):
		try:
			if len(self.unsorted_array) == 0:
				self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
			else:
				self.disable_button()
				t = np.arange(len(self.unsorted_array))
				array = self.unsorted_array
				self.QuickSort(array, 0, len(self.unsorted_array) - 1)
				self.ui.MplSort.canvas.axes.clear()
				self.ui.MplSort.canvas.axes.set_title("Quick Sort Animation", loc='left')
				self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
															 edgecolor="#f0f8ff")

				self.autolabel(self.rects)
				self.ui.MplSort.canvas.axes.patch.set_alpha(0)
				self.ui.MplSort.canvas.draw()
				self.enable_button()
		except AttributeError:
			self.msg = QMessageBox.critical(self, "Error",
											"Please make the operations in order!\nMake sure to set to Array Size and Range")
			self.enable_button()

	def QuickSort(self, array, p, r):
		if p < r:
			q = self.partition(array, p, r)
			self.QuickSort(array, p, q - 1)
			self.QuickSort(array, q + 1, r)

	def partition(self, array, p, r):
		t = np.arange(len(self.unsorted_array))
		pivotelement = array[r]
		i = p - 1
		for j in range(p, r):
			if array[j] <= pivotelement:
				i += 1

				array[i], array[j] = array[j], array[i]
				self.ui.MplSort.canvas.axes.clear()
				self.ui.MplSort.canvas.axes.set_title("Quick Sort Animation", loc='left')
				self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
															 edgecolor="#f0f8ff")
				self.autolabel(self.rects)
				self.operation_buttons()
				self.rects = self.ui.MplSort.canvas.axes.bar(t[j], self.unsorted_array[j], color="black",
															 edgecolor="black")
				self.autolabel(self.rects)
				self.rects = self.ui.MplSort.canvas.axes.bar(t[j + 1], self.unsorted_array[j + 1], color="blue",
															 edgecolor="black")
				self.autolabel(self.rects)
				self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="black",
															 edgecolor="black")
				self.autolabel(self.rects)
				self.ui.MplSort.canvas.axes.patch.set_alpha(0)
				self.ui.MplSort.canvas.draw()
				self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
				time.sleep(self.speedofproject)
				QApplication.processEvents()

			self.ui.MplSort.canvas.axes.clear()
			self.ui.MplSort.canvas.axes.set_title("Quick Sort Animation", loc='left')
			self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a', edgecolor="#f0f8ff")
			self.autolabel(self.rects)
			self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="blue", edgecolor="black")
			self.autolabel(self.rects)
			self.rects = self.ui.MplSort.canvas.axes.bar(t[j + 1], self.unsorted_array[j + 1], color="black",
														 edgecolor="black")
			self.autolabel(self.rects)
			self.rects = self.ui.MplSort.canvas.axes.bar(t[r], self.unsorted_array[r], color="red", edgecolor="black")
			self.autolabel(self.rects)
			self.ui.MplSort.canvas.axes.patch.set_alpha(0)
			self.ui.MplSort.canvas.draw()
			self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
			time.sleep(self.speedofproject)
			QApplication.processEvents()
		array[i + 1], array[r] = array[r], array[i + 1]

		return i + 1

	# %% Heap Sort Animation

	def Heapify(self, array, n, i):
		largest = i
		left = 2 * i + 1
		right = 2 * i + 2

		if left < n and array[i] < array[left]:
			largest = left
		if right < n and array[largest] < array[right]:
			largest = right
		if largest != i:
			array[i], array[largest] = array[largest], array[i]
			self.Heapify(array, n, largest)

	def HeapSort(self):
		try:
			if len(self.unsorted_array) == 0:
				self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
			else:
				self.disable_button()
				t = np.arange(len(self.unsorted_array))
				n = len(self.unsorted_array)
				for i in range(n // 2 - 1, -1, -1):
					self.Heapify(self.unsorted_array, n, i)
					self.ui.MplSort.canvas.axes.clear()
					self.operation_buttons()
					self.ui.MplSort.canvas.axes.set_title("Heap Sort Animation", loc='left')
					self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
																 edgecolor="#f0f8ff")
					self.autolabel(self.rects)
					self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="black",
																 edgecolor="black")
					self.autolabel(self.rects)
					self.ui.MplSort.canvas.axes.patch.set_alpha(0)
					self.ui.MplSort.canvas.draw()
					self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
					time.sleep(self.speedofproject)
					QApplication.processEvents()

				for i in range(n - 1, 0, -1):
					self.unsorted_array[i], self.unsorted_array[0] = self.unsorted_array[0], self.unsorted_array[i]
					self.Heapify(self.unsorted_array, i, 0)
					self.ui.MplSort.canvas.axes.clear()
					self.ui.MplSort.canvas.axes.set_title("Heap Sort Animation", loc='left')
					self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
																 edgecolor="#f0f8ff")
					self.autolabel(self.rects)
					self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="black",
																 edgecolor="black")
					self.autolabel(self.rects)
					self.ui.MplSort.canvas.axes.patch.set_alpha(0)
					self.ui.MplSort.canvas.draw()
					self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
					time.sleep(self.speedofproject)
					QApplication.processEvents()

				self.ui.MplSort.canvas.axes.clear()
				self.ui.MplSort.canvas.axes.set_title("Heap Sort Animation", loc='left')
				self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
															 edgecolor="#f0f8ff")
				self.autolabel(self.rects)
				self.ui.MplSort.canvas.axes.patch.set_alpha(0)
				self.ui.MplSort.canvas.draw()
				self.enable_button()
		except AttributeError:
			self.msg = QMessageBox.critical(self, "Error",
											"Please make the operations in order!\nMake sure to set to Array Size and Range")
			self.enable_button()

	# %% Counting Sort Animation
	def CountingSort(self):
		try:
			if len(self.unsorted_array) == 0:
				self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
			else:
				self.disable_button()
				t = np.arange(len(self.unsorted_array))
				max_value = int(max(self.unsorted_array))
				min_value = int(min(self.unsorted_array))
				range_of_elements = max_value - min_value + 1

				counting_temp_array = [0 for _ in range(range_of_elements)]
				sorted_array = [0 for _ in range(len(self.unsorted_array))]

				for i in range(0, len(self.unsorted_array)):
					counting_temp_array[self.unsorted_array[i] - min_value] += 1

				for i in range(1, len(counting_temp_array)):
					counting_temp_array[i] += counting_temp_array[i - 1]

				for i in range(len(self.unsorted_array) - 1, -1, -1):
					sorted_array[counting_temp_array[self.unsorted_array[i] - min_value] - 1] = self.unsorted_array[i]
					counting_temp_array[self.unsorted_array[i] - min_value] -= 1
					self.operation_buttons()

				for i in range(len(self.unsorted_array) - 1):
					self.ui.MplSort.canvas.axes.clear()
					self.ui.MplSort.canvas.axes.set_title("Counting Sort Animation", loc='left')
					self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
																 edgecolor="#f0f8ff")
					self.autolabel(self.rects)
					self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="red",
																 edgecolor="black")
					self.autolabel(self.rects)
					self.ui.MplSort.canvas.axes.patch.set_alpha(0)
					self.ui.MplSort.canvas.draw()
					self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
					time.sleep(self.speedofproject)
					QApplication.processEvents()

				for i in range(0, len(self.unsorted_array)):
					self.unsorted_array[i] = sorted_array[i]
					self.ui.MplSort.canvas.axes.clear()
					self.ui.MplSort.canvas.axes.set_title("Counting Sort Animation", loc='left')
					self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
																 edgecolor="#f0f8ff")
					self.autolabel(self.rects)
					self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="black",
																 edgecolor="black")
					self.autolabel(self.rects)
					self.ui.MplSort.canvas.axes.patch.set_alpha(0)
					self.ui.MplSort.canvas.draw()
					self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
					time.sleep(self.speedofproject)
					QApplication.processEvents()
				self.ui.MplSort.canvas.axes.clear()
				self.ui.MplSort.canvas.axes.set_title("Counting Sort Animation", loc='left')
				self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
															 edgecolor="#f0f8ff")
				self.autolabel(self.rects)
				self.ui.MplSort.canvas.axes.patch.set_alpha(0)
				self.ui.MplSort.canvas.draw()
				self.enable_button()

		except AttributeError:
			self.msg = QMessageBox.critical(self, "Error",
											"Please make the operations in order!\nMake sure to set to Array Size and Range")
			self.enable_button()

	# %% Bucket Sort Animation
	def BucketSort(self):
		try:
			if len(self.unsorted_array) == 0:
				self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
			else:
				self.disable_button()
				t = np.arange(len(self.unsorted_array))
				max_value = max(self.unsorted_array)
				size = max_value / len(self.unsorted_array)

				buckets_list = []
				for x in range(len(self.unsorted_array)):
					buckets_list.append([])

				for i in range(len(self.unsorted_array)):
					j = int(self.unsorted_array[i] / size)
					if j != len(self.unsorted_array):
						buckets_list[j].append(self.unsorted_array[i])

					else:
						buckets_list[len(self.unsorted_array) - 1].append(self.unsorted_array[i])

				for z in range(len(self.unsorted_array)):
					binarysearch.insertion_sort(buckets_list[z])

				final_output = []
				for x in range(len(self.unsorted_array)):
					final_output = final_output + buckets_list[x]
					self.operation_buttons()

				for i in range(len(self.unsorted_array) - 1):
					self.ui.MplSort.canvas.axes.clear()
					self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
																 edgecolor="#f0f8ff")
					self.autolabel(self.rects)
					self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="black",
																 edgecolor="black")
					self.autolabel(self.rects)
					self.ui.MplSort.canvas.axes.patch.set_alpha(0)
					self.ui.MplSort.canvas.draw()
					self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
					time.sleep(self.speedofproject)
					QApplication.processEvents()

				for i in range(0, len(self.unsorted_array)):
					self.unsorted_array[i] = final_output[i]
					self.ui.MplSort.canvas.axes.clear()
					self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
																 edgecolor="#f0f8ff")
					self.autolabel(self.rects)
					self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="gray",
																 edgecolor="black")
					self.autolabel(self.rects)
					self.ui.MplSort.canvas.axes.patch.set_alpha(0)
					self.ui.MplSort.canvas.draw()
					self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
					time.sleep(self.speedofproject)
					QApplication.processEvents()

				self.enable_button()
		except AttributeError:
			self.msg = QMessageBox.critical(self, "Error",
											"Please make the operations in order!\nMake sure to set to Array Size and Range")
			self.enable_button()

	# %% Shell Sort Animation
	def ShellSort(self):
		try:
			if len(self.unsorted_array) == 0:
				self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
			else:
				self.disable_button()
				t = np.arange(len(self.unsorted_array))
				n = len(self.unsorted_array)
				gap = n // 2

				while gap > 0:
					for i in range(gap, n):
						temp = self.unsorted_array[i]
						j = i
						self.ui.MplSort.canvas.axes.clear()
						self.ui.MplSort.canvas.axes.set_title("Shell Sort Animation", loc='left')
						self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
																	 edgecolor="#f0f8ff")
						self.autolabel(self.rects)
						self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="red",
																	 edgecolor="black")
						self.autolabel(self.rects)
						self.ui.MplSort.canvas.axes.patch.set_alpha(0)
						self.ui.MplSort.canvas.draw()
						self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
						time.sleep(self.speedofproject)
						QApplication.processEvents()
						while j >= gap and self.unsorted_array[j - gap] > temp:
							self.unsorted_array[j] = self.unsorted_array[j - gap]
							self.ui.MplSort.canvas.axes.clear()
							self.ui.MplSort.canvas.axes.set_title("Shell Sort Animation", loc='left')
							self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
																		 edgecolor="#f0f8ff")
							self.autolabel(self.rects)
							self.rects = self.ui.MplSort.canvas.axes.bar(t[j], self.unsorted_array[j], color="blue",
																		 edgecolor="black")
							self.autolabel(self.rects)
							self.ui.MplSort.canvas.axes.patch.set_alpha(0)
							self.ui.MplSort.canvas.draw()
							self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
							time.sleep(self.speedofproject)
							QApplication.processEvents()
							j -= gap
						self.unsorted_array[j] = temp
					gap //= 2
					self.operation_buttons()

				self.ui.MplSort.canvas.axes.clear()
				self.ui.MplSort.canvas.axes.set_title("Shell Sort Animation", loc='left')
				self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
															 edgecolor="#f0f8ff")
				self.autolabel(self.rects)
				self.ui.MplSort.canvas.axes.patch.set_alpha(0)
				self.ui.MplSort.canvas.draw()
				self.enable_button()
		except AttributeError:
			self.msg = QMessageBox.critical(self, "Error",
											"Please make the operations in order!\nMake sure to set to Array Size and Range")
			self.enable_button()

	# %% Radix Sort Animation
	def countingSort(self, array, digit):
		count = []
		result_array = []
		j = len(array) - 1
		for i in range(10):
			count.append(0)
		for i in range(len(array)):
			result_array.append(0)
		for i in range(len(array)):
			count[(array[i] // digit) % 10] += 1
		for i in range(len(count)):
			if i > 0:
				count[i] += count[i - 1]
		for i in range(len(array)):
			count[(array[j] // digit) % 10] -= 1
			result_array[count[(array[j] // digit) % 10]] = array[j]
			j -= 1
			t = np.arange(len(result_array))
			self.ui.MplSort.canvas.axes.clear()
			self.ui.MplSort.canvas.axes.set_title("Counting Sort Animation", loc='left')
			self.rects = self.ui.MplSort.canvas.axes.bar(t, result_array, color='#56132a', edgecolor="#f0f8ff")
			self.autolabel(self.rects)
			self.rects = self.ui.MplSort.canvas.axes.bar(t[i], result_array[i], color="red", edgecolor="black")
			self.autolabel(self.rects)
			self.ui.MplSort.canvas.axes.patch.set_alpha(0)
			self.ui.MplSort.canvas.draw()
			self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
			time.sleep(self.speedofproject)
			QApplication.processEvents()
		for i in range(len(array)):
			array[i] = result_array[i]

	def RadixSort(self):
		try:
			if len(self.unsorted_array) == 0:
				self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
			else:
				self.disable_button()
				t = np.arange(len(self.unsorted_array))
				max_number = max(self.unsorted_array)
				digit = 1
				while max_number // digit > 0:
					self.countingSort(self.unsorted_array, digit)
					digit *= 10
					self.operation_buttons()
				self.ui.MplSort.canvas.axes.clear()
				self.ui.MplSort.canvas.axes.set_title("Counting Sort Animation", loc='left')
				self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
															 edgecolor="#f0f8ff")
				self.autolabel(self.rects)
				self.ui.MplSort.canvas.axes.patch.set_alpha(0)
				self.ui.MplSort.canvas.draw()
				self.enable_button()
		except AttributeError:
			self.msg = QMessageBox.critical(self, "Error",
											"Please make the operations in order!\nMake sure to set to Array Size and Range")
			self.enable_button()

	# %% Cocktail Sort Algorithm
	def CoctailSort(self):
		try:
			if len(self.unsorted_array) != 0:
				t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
				self.disable_button()
				isSwapped = True
				start = 0
				end = len(self.unsorted_array) - 1
				while (isSwapped == True):
					isSwapped = False
					for i in range(start, end):
						if (self.unsorted_array[i] > self.unsorted_array[i + 1]):
							self.unsorted_array[i], self.unsorted_array[i + 1] = self.unsorted_array[i + 1], \
																				 self.unsorted_array[i]
							isSwapped = True
						self.ui.MplSort.canvas.axes.clear()
						self.ui.MplSort.canvas.axes.set_title("Cocktail Sort Animation", loc="left", color="white")
						self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
																	 edgecolor="#f0f8ff")
						self.autolabel(self.rects)
						self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="#800000",
																	 edgecolor="green")
						self.autolabel(self.rects)
						self.ui.MplSort.canvas.axes.patch.set_alpha(0)

						self.ui.MplSort.canvas.draw()
						self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
						time.sleep(self.speedofproject)
						QApplication.processEvents()
					if (isSwapped == False):
						break
					isSwapped = False
					end = end - 1

					for i in range(end - 1, start - 1, -1):
						if (self.unsorted_array[i] > self.unsorted_array[i + 1]):
							self.unsorted_array[i], self.unsorted_array[i + 1] = self.unsorted_array[i + 1], \
																				 self.unsorted_array[i]
							isSwapped = True
						self.ui.MplSort.canvas.axes.clear()
						self.ui.MplSort.canvas.axes.set_title("Cocktail Sort Animation", loc="left", color="white")
						self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color=['#583d72'],
																	 edgecolor='blue')
						self.autolabel(self.rects)
						self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="#000080",
																	 edgecolor="green")
						self.autolabel(self.rects)
						self.ui.MplSort.canvas.axes.patch.set_alpha(0)
						self.ui.MplSort.canvas.draw()
						self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
						time.sleep(self.speedofproject)
						QApplication.processEvents()
					start = start + 1
				self.ui.MplSort.canvas.axes.clear()
				self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
															 edgecolor="#f0f8ff")
				self.autolabel(self.rects)
				self.ui.MplSort.canvas.axes.patch.set_alpha(0)
				self.ui.MplSort.canvas.draw()
				self.enable_button()
			else:
				self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
		except AttributeError:
			self.msg = QMessageBox.critical(self, "Error",
											"Please make the operations in order!\nMake sure to set to Array Size and Range")
			self.enable_button()

	# %%Comb Sort Animation

	def callcombsort(self):
		try:
			if len(self.unsorted_array) != 0:
				t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
				self.disable_button()
				self.combsort(self.unsorted_array)
				self.ui.MplSort.canvas.axes.clear()
				self.ui.MplSort.canvas.axes.set_title("Comb Sort Animation", loc='left')
				self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
															 edgecolor="#f0f8ff")

				self.autolabel(self.rects)
				self.ui.MplSort.canvas.axes.patch.set_alpha(0)
				self.ui.MplSort.canvas.draw()
				self.enable_button()

		except AttributeError:
			self.msg = QMessageBox.critical(self, "Error",
											"Please make the operations in order!\nMake sure to set to Array Size and Range")
			self.enable_button()

	def combsort(self, array):
		t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
		gap = len(array)
		swaps = True
		while gap > 1 or swaps:
			gap = max(1, int(gap / 1.25))
			swaps = False
			for i in range(len(array) - gap):
				self.ui.MplSort.canvas.axes.clear()
				self.ui.MplSort.canvas.axes.set_title("Comb Sort Animation", loc="left", color="white")
				self.rects = self.ui.MplSort.canvas.axes.bar(t, array, color='#56132a', edgecolor="#f0f8ff")
				self.autolabel(self.rects)
				self.rects = self.ui.MplSort.canvas.axes.bar(t[i], array[i], color="#FFE4E1", edgecolor="black")
				self.autolabel(self.rects)
				self.ui.MplSort.canvas.axes.patch.set_alpha(0)
				self.ui.MplSort.canvas.draw()
				self.speedofproject = 0.001 * (100 - self.ui.verticalSlider.value())
				time.sleep(self.speedofproject)
				QApplication.processEvents()
				j = i + gap
				if array[i] > array[j]:
					array[i], array[j] = array[j], array[i]
					swaps = True

	# %% Clear Button
	def clear(self):
		self.ui.displayarrays_sort.clear()
		self.lower = 0
		self.upper = 0
		self.length = 0
		self.ui.lower_range.clear()
		self.ui.upper_range.clear()
		self.ui.array_sort.setValue(0)
		self.unsorted_array = []
		self.ui.MplSort.canvas.axes.clear()
		self.ui.MplSort.canvas.axes.patch.set_alpha(0)
		self.ui.MplSort.canvas.draw()


# %% Initialization
if __name__ == "__main__":
	app = QApplication([])
	window = SortingAlgorithms()
	window.show()
	sys.exit(app.exec_())
