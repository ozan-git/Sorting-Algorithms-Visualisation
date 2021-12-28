# Introduction to Algorithm course graphical interface design project time comparison page.
# 5 December 2021.
# Written by Orhan Ozan Yildiz.

import sys

import speech_recognition as sr
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from uiqt_time_comparison import Ui_MainWindow
from utils_operations import timer

times = timer()


# %%
class TimeComparisonMainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ui.comparisonchoosen_button.setText("Comparison Chosen Algorithms")
		self.method_list = [False, False, False, False, False, False, False, False, False, False]
		self.setWindowTitle('Time Comparison')
		self.ui.clear_btn.clicked.connect(self.clear)
		self.ui.back_btn.clicked.connect(self.close)

		self.ui.comparisonall_button.pressed.connect(self.compare_all)
		self.ui.comparisonchoosen_button.pressed.connect(self.compare_chosen)

		# self.ui.mic_btn.clicked.connect(self.voice)

		self.ui.bubblesort_checkBox.toggled.connect(self.checkbox_toggled)
		self.ui.insertionsort_checkBox.toggled.connect(self.checkbox_toggled)
		self.ui.mergesort_checkBox.toggled.connect(self.checkbox_toggled)
		self.ui.selectionsort_checkBox.toggled.connect(self.checkbox_toggled)
		self.ui.countingsort_checkBox.toggled.connect(self.checkbox_toggled)
		self.ui.heapsort_checkBox.toggled.connect(self.checkbox_toggled)
		self.ui.bucketsort_checkBox.toggled.connect(self.checkbox_toggled)
		self.ui.radixsort_checkBox.toggled.connect(self.checkbox_toggled)
		self.ui.quicksort_checkBox.toggled.connect(self.checkbox_toggled)
		self.ui.shellsort_checkBox.toggled.connect(self.checkbox_toggled)
		self.ui.MplSort.canvas.axes.set_title('Time Comparison Graph')
		self.ui.MplSort.canvas.axes.set_xlabel('Number of elements in array')
		self.ui.MplSort.canvas.axes.set_ylabel('Time')

		self.ui.btn_close.clicked.connect(self.close)
		self.ui.btn_maximize_restore.clicked.connect(self.showMaximized)
		self.ui.btn_minimize.clicked.connect(self.showMinimized)

		self.setWindowFlags(Qt.CustomizeWindowHint)
		self.pressing = False

	def resizeEvent(self, QResizeEvent):
		super(TimeComparisonMainWindow, self).resizeEvent(QResizeEvent)
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

	# %%
	def voice(self):
		r = sr.Recognizer()
		microphoneValue = ""
		with sr.Microphone() as source:
			try:
				self.statusBar().showMessage('Start talking...')
				audio = r.listen(source)
				microphoneValue = (r.recognize_google(audio))
				self.statusBar().showMessage('Stop talking...')
				print(microphoneValue)
				try:
					if microphoneValue == 'comparison all':
						try:
							self.compare_all()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")
					elif microphoneValue == 'comparison chosen methods':
						try:
							self.compare_chosen()
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

		# %%

	def compare_all(self):
		all_methods = times.comparison([True, True, True, True, True, True, True, True, True, True])
		algorithms = ["Bubble", "Insertion", "Merge", "Selection", "Counting", "Heap", "Bucket", "Radix", "Quick",
					  "Shell"]
		methods_list = []
		for i in algorithms:
			methods_list.append(all_methods[i])

		colors_graph = ["#e60000", "#114477", "#223300", "#F1A1D8", "#BCF199", "#F9E16D", "#03F5DF", "#B303F5",
						"#03F512", "#064564"]
		k = 0
		self.ui.MplSort.canvas.axes.clear()
		for i in methods_list:
			self.ui.MplSort.canvas.axes.plot([100, 300, 500, 2000], i, color=colors_graph[k], label=algorithms[k])
			self.ui.MplSort.canvas.axes.legend(algorithms, loc="upper left")
			self.ui.MplSort.canvas.draw()
			k += 1

	def compare_chosen(self):
		if not (self.method_list[0] or self.method_list[1] or self.method_list[2] or self.method_list[3] or
				self.method_list[4] or self.method_list[5] or self.method_list[6] or self.method_list[7] or
				self.method_list[8]):
			QMessageBox.critical(self, "ERROR", "Please choose a method/methods to compare...")
		else:

			algorithms = []
			algorithms_counter = 0
			if self.method_list[0]:
				algorithms.append("Bubble")
				algorithms_counter += 1
			if self.method_list[1]:
				algorithms.append("Insertion")
				algorithms_counter += 1
			if self.method_list[2]:
				algorithms.append("Merge")
				algorithms_counter += 1
			if self.method_list[3]:
				algorithms.append("Selection")
				algorithms_counter += 1
			if self.method_list[4]:
				algorithms.append("Counting")
				algorithms_counter += 1
			if self.method_list[5]:
				algorithms.append("Heap")
				algorithms_counter += 1
			if self.method_list[6]:
				algorithms.append("Bucket")
				algorithms_counter += 1
			if self.method_list[7]:
				algorithms.append("Radix")
				algorithms_counter += 1
			if self.method_list[8]:
				algorithms.append("Quick")
				algorithms_counter += 1
			if self.method_list[9]:
				algorithms.append("Shell")
				algorithms_counter += 1

			chosen_methods = times.comparison(self.method_list)
			methods_list = []
			for i in algorithms:
				methods_list.append(chosen_methods[i])

			colors_graph = ["#e60000", "#114477", "#223300", "#F1A1D8", "#BCF199", "#F9E16D", "#03F5DF", "#B303F5",
							"#03F512"]
			k = 0
			self.ui.MplSort.canvas.axes.clear()
			for i in methods_list:
				# self.ui.MplWidget_fibonacci.canvas.axes.clear()
				self.ui.MplSort.canvas.axes.plot([100, 300, 500, 2000], i, color=colors_graph[k], label=algorithms[k])
				self.ui.MplSort.canvas.axes.legend(algorithms, loc="upper left")
				self.ui.MplSort.canvas.draw()
				k += 1

	def checkbox_toggled(self):

		if self.ui.bubblesort_checkBox.isChecked():
			self.method_list[0] = True
		else:
			self.method_list[0] = False
		if self.ui.insertionsort_checkBox.isChecked():
			self.method_list[1] = True
		else:
			self.method_list[1] = False
		if self.ui.mergesort_checkBox.isChecked():
			self.method_list[2] = True
		else:
			self.method_list[2] = False
		if self.ui.selectionsort_checkBox.isChecked():
			self.method_list[3] = True
		else:
			self.method_list[3] = False
		if self.ui.countingsort_checkBox.isChecked():
			self.method_list[4] = True
		else:
			self.method_list[4] = False
		if self.ui.heapsort_checkBox.isChecked():
			self.method_list[5] = True
		else:
			self.method_list[5] = False
		if self.ui.bucketsort_checkBox.isChecked():
			self.method_list[6] = True
		else:
			self.method_list[6] = False
		if self.ui.radixsort_checkBox.isChecked():
			self.method_list[7] = True
		else:
			self.method_list[7] = False
		if self.ui.quicksort_checkBox.isChecked():
			self.method_list[8] = True
		else:
			self.method_list[8] = False
		if self.ui.shellsort_checkBox.isChecked():
			self.method_list[9] = True
		else:
			self.method_list[9] = False

	# %% Clear Button

	def clear(self):
		self.ui.bubblesort_checkBox.setChecked(False)
		self.ui.insertionsort_checkBox.setChecked(False)
		self.ui.mergesort_checkBox.setChecked(False)
		self.ui.selectionsort_checkBox.setChecked(False)
		self.ui.countingsort_checkBox.setChecked(False)
		self.ui.heapsort_checkBox.setChecked(False)
		self.ui.bucketsort_checkBox.setChecked(False)
		self.ui.radixsort_checkBox.setChecked(False)
		self.ui.quicksort_checkBox.setChecked(False)
		self.ui.shellsort_checkBox.setChecked(False)
		self.ui.MplSort.canvas.axes.clear()
		self.ui.MplSort.canvas.draw()

	# %% Initialization


if __name__ == "__main__":
	app = QApplication([])
	window = TimeComparisonMainWindow()
	window.show()
	sys.exit(app.exec_())
