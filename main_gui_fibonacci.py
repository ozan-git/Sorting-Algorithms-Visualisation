# Introduction to Algorithm course graphical interface design project fibonacci page.
# 5 December 2021.

# Written by Orhan Ozan Yildiz.
import math
import sys
import turtle

import numpy as np
import speech_recognition as sr
from PyQt5.QtGui import QIntValidator
# %% including required libraries, modules and files with code
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from uiqt_fibonacci import Ui_FibonacciWindow
from utils_operations import fibonacci

fibonacci = fibonacci()


# %% Application Content
class Fibonacci(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_FibonacciWindow()  # Ability to use the class in which the interface I designed with qt designer converted into code
		self.ui.setupUi(self)
		self.ui.back_btn.clicked.connect(self.close)  # Back to my home page linking with the back button
		self.ui.n_number.setValidator(
			QIntValidator(1, 1000, self))  # fixing the number received from the user to the integer
		self.ui.findfibo_btn.clicked.connect(self.fibo_number)  # Connecting the fibonacci find function with the button
		self.ui.findfibo_btn.clicked.connect(
			self.fibo_bar_graph)  # Connecting the same button with the function that I have graphed
		self.ui.MplFib.canvas.axes.get_xaxis().set_visible(False)
		self.ui.MplFib.canvas.axes.get_yaxis().set_visible(False)
		self.ui.golden_spiral.clicked.connect(self.spiral)
		self.ui.mic_btn.clicked.connect(self.voice)
		self.ui.clear_btn.clicked.connect(self.clear)
		self.ui.horizontalSlider.valueChanged.connect(self.value)

	def value(self):
		self.n = self.ui.horizontalSlider.value()
		self.ui.lineEdit.setText(str(self.n))

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
					if microphoneValue == 'find':
						try:
							self.fibo_number()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")
					elif microphoneValue == 'Fibonacci spiral':
						try:
							self.spiral()
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

	def error(self):
		self.n = int(self.ui.n_number.text())
		if self.n == 0:
			self.ui.MplFib.canvas.axes.clear()
			self.ui.MplFib.canvas.draw()
			self.msg = QMessageBox.critical(self, "Error", "Please enter a positive integer!")
		else:
			pass

	def fibo_number(self):
		try:
			self.n = int(self.ui.n_number.text())  # User input with line edit
			if self.n == 0:
				self.ui.MplFib.canvas.axes.clear()
				self.ui.MplFib.canvas.axes.patch.set_alpha(0)
				self.ui.MplFib.canvas.draw()
				self.msg = QMessageBox.critical(self, "Error", "Please enter a positive integer!")
			else:  # Function of finding a fibonacci number
				self.result = fibonacci.fibonacci_number(
					self.n)  # sending this number to the function in my project operations file
				self.ui.result.setText("{}. Fibonacci Number is {}".format(str(self.n),
																		   str(self.result)))  # the result appears on the screen
				self.fibonacci_numbers = fibonacci.fibonacci_array(self.n)
				self.ui.fibonacci_series.setText(str(self.fibonacci_numbers))
		except ValueError:
			self.msg = QMessageBox.critical(self, "Error", "Please enter a positive integer!")

	# %%
	def fibo_bar_graph(self):
		self.n = int(self.ui.n_number.text())
		if self.n == 0:
			self.ui.MplFib.canvas.axes.clear()
		# self.msg=QMessageBox.critical(self,"Error","Please enter a positive integer!")
		else:
			self.x = np.arange(1, self.n + 1)  # assigning x-axis numbers to the chart
			self.y = fibonacci.fibonacci_array(self.n)  # assigning fibonacci numbers to the y-axis of the chart
			self.x_pos = [i for i, _ in enumerate(self.x)]
			self.ui.MplFib.canvas.axes.clear()  # cleaning the graphic display before each drawing
			self.rects = self.ui.MplFib.canvas.axes.bar(self.x_pos, self.y, color='#56132a', edgecolor="#f0f8ff")
			self.autolabel(self.rects)
			self.ui.MplFib.canvas.axes.patch.set_alpha(0)
			self.ui.MplFib.canvas.axes.set_title('Fibonacci Graph')
			self.ui.MplFib.canvas.draw()  # plotting the graph

	def autolabel(self, rects):  # The function for writing number values ​​on the bar graph
		for rect in self.rects:
			height = rect.get_height()
			self.ui.MplFib.canvas.axes.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
											'%d' % int(height),
											ha='center', va='bottom')

	# %%
	def golden_spiral(self):
		a = 0
		b = 1
		square_a = a
		square_b = b

		# Setting the colour of the plotting pen to blue
		self.x.pencolor("blue")

		# Drawing the first square
		self.x.forward(b * self.factor)
		self.x.left(90)
		self.x.forward(b * self.factor)
		self.x.left(90)
		self.x.forward(b * self.factor)
		self.x.left(90)
		self.x.forward(b * self.factor)

		# Proceeding in the Fibonacci Series
		temp = square_b
		square_b = square_b + square_a
		square_a = temp

		# Drawing the rest of the squares
		for i in range(1, self.n):
			self.x.backward(square_a * self.factor)
			self.x.right(90)
			self.x.forward(square_b * self.factor)
			self.x.left(90)
			self.x.forward(square_b * self.factor)
			self.x.left(90)
			self.x.forward(square_b * self.factor)

			# Proceeding in the Fibonacci Series
			temp = square_b
			square_b = square_b + square_a
			square_a = temp

		# Bringing the pen to starting point of the spiral plot
		self.x.penup()
		self.x.setposition(self.factor, 0)
		self.x.seth(0)
		self.x.pendown()

		# Setting the colour of the plotting pen to red
		self.x.pencolor("red")

		# Fibonacci Spiral Plot
		self.x.left(90)
		for i in range(self.n):
			print(b)
			fdwd = math.pi * b * self.factor / 2
			fdwd /= 90
			for j in range(90):
				self.x.forward(fdwd)
				self.x.left(1)
			temp = a
			a = b
			b = temp + b

	def spiral(self):
		self.factor = 1
		self.n = self.ui.horizontalSlider.value()
		self.ui.lineEdit.setText(str(self.n))
		self.x = turtle.Turtle()
		self.x.speed(100)
		self.golden_spiral()
		turtle.done()

	# %%
	def clear(self):
		self.ui.n_number.clear()
		self.ui.result.clear()
		self.ui.horizontalSlider.setValue(1)
		self.ui.MplFib.canvas.axes.clear()
		self.ui.MplFib.canvas.axes.patch.set_alpha(0)
		self.ui.MplFib.canvas.draw()
		self.ui.fibonacci_series.clear()


# %% Initialization
if __name__ == "__main__":
	app = QApplication([])
	window = Fibonacci()
	window.show()
	sys.exit(app.exec_())
