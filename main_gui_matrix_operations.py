# Introduction to Algorithm course graphical interface design project matrix operations page.
# 5 December 2021.

# Written by Orhan Ozan Yildiz.

import math
import sys
import time

import numpy as np
import speech_recognition as sr
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from uiqt_matrix_operations import Ui_MatrixWindow
from utils_operations import createamatrix, matrix_mult

create_matrix = createamatrix()
matrix_mult = matrix_mult()


# %% Application Content
class MatrixOperation(QMainWindow):
	def __init__(self):
		super().__init__()
		# The variable created so that the interface class can be used.
		self.ui = Ui_MatrixWindow()
		self.ui.setupUi(self)
		self.setWindowTitle('Matrix Operations')
		# linking the first line edit for matrix 1 to the inputs function with the enter key
		# linking the second line for matrix 1 edit to the inputs function with the enter key
		# linking the first line edit for matrix 2 to the inputs function with the enter key
		# linking the second line edit for matrix 2 to the inputs function with the enter key
		self.ui.row_m1.returnPressed.connect(self.inputs)
		self.ui.column_m1.returnPressed.connect(self.inputs)
		self.ui.row_m2.returnPressed.connect(self.inputs)
		self.ui.column_m2.returnPressed.connect(self.inputs)

		# The value taken from the first line edit for matrix 1 is an integer and is fixed between 1 and 15
		# The value taken from the second line edit for matrix 1 is an integer and is fixed between 1 and 15
		# The value taken from the first line edit for matrix 2 is an integer and is fixed between 1 and 15
		# The value taken from the first line edit for matrix 2 is an integer and is fixed between 1 and 15
		self.ui.row_m1.setValidator(QIntValidator(0, 10, self))
		self.ui.column_m1.setValidator(QIntValidator(0, 10, self))
		self.ui.row_m2.setValidator(QIntValidator(0, 10, self))
		self.ui.column_m2.setValidator(QIntValidator(0, 10, self))

		self.ui.create_matrix_btn_1.clicked.connect(self.matrix1_user)
		self.ui.create_matrix_btn_2.clicked.connect(self.matrix2_user)
		self.ui.back_btn.clicked.connect(self.close)

		# Adding functionality to generate matrix button with random matrices function
		# Adding functionality to multiply button with multiplication function
		self.ui.generate_matrix_btn.clicked.connect(self.random_matrices)
		self.ui.multiply_btn.clicked.connect(self.multiplication)

		# Adding functionality to clear button with clear function
		self.ui.clear_btn.clicked.connect(self.clear)
		self.ui.determinant_btn_1.clicked.connect(self.determinant1)
		self.ui.determinant_btn_2.clicked.connect(self.determinant2)
		self.ui.inverse_btn_1.clicked.connect(self.inverse1)
		self.ui.inverse_btn_2.clicked.connect(self.inverse2)
		self.ui.transpose_btn_1.clicked.connect(self.transpose1)
		self.ui.transpose_btn_2.clicked.connect(self.transpose2)
		self.ui.rank_btn_1.clicked.connect(self.rank1)
		self.ui.rank_btn_2.clicked.connect(self.rank2)
		self.ui.multiplyby_btn.clicked.connect(self.mult_scalar1)
		self.ui.multiplyby_btn_2.clicked.connect(self.mult_scalar2)
		self.visible1_false()
		self.visible2_false()
		self.ui.mic_btn.clicked.connect(self.voice)

		self.ui.btn_close.clicked.connect(self.close)
		self.ui.btn_maximize_restore.clicked.connect(self.showMaximized)
		self.ui.btn_minimize.clicked.connect(self.showMinimized)

		self.setWindowFlags(Qt.CustomizeWindowHint)
		self.pressing = False

	def resizeEvent(self, QResizeEvent):
		super(MatrixOperation, self).resizeEvent(QResizeEvent)
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

	# %% Voice.
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
					if microphoneValue == 'random Matrix':
						try:
							self.random_matrices()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")
					elif microphoneValue == 'multiply':
						try:
							self.multiplication()
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
					elif microphoneValue == 'create Matrix one':
						try:
							self.matrix1_user()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")
					elif microphoneValue == 'create Matrix two':
						try:
							self.matrix2_user()
							microphoneValue = ""
						except:
							QMessageBox.warning(self, "ERROR", "Try Again...")

					elif self.ui.determinant_btn_1.isVisible():
						if microphoneValue == 'determinant Matrix 1':
							try:
								self.determinant1()
								microphoneValue = ""
							except:
								QMessageBox.warning(self, "ERROR", "Try Again...")

						elif microphoneValue == 'inverse Matrix one':
							try:
								self.inverse1()
								microphoneValue = ""
							except:
								QMessageBox.warning(self, "ERROR", "Try Again...")
						elif microphoneValue == 'transpose Matrix one':
							try:
								self.transpose1()
								microphoneValue = ""
							except:
								QMessageBox.warning(self, "ERROR", "Try Again...")
						elif microphoneValue == 'rank Matrix one':
							try:
								self.rank1()
								microphoneValue = ""
							except:
								QMessageBox.warning(self, "ERROR", "Try Again...")
						elif microphoneValue == 'multiply Matrix one':
							try:
								self.mult_scalar1()
								microphoneValue = ""
							except:
								QMessageBox.warning(self, "ERROR", "Try Again...")
						else:
							QMessageBox.warning(self, "ERROR", "Try Again...")

					elif self.ui.determinant_btn_2.isVisible:
						if microphoneValue == 'determinant Matrix two':
							try:
								self.determinant2()
								microphoneValue = ""
							except:
								QMessageBox.warning(self, "ERROR", "Try Again...")
						elif microphoneValue == 'inverse Matrix two':
							try:
								self.inverse2()
								microphoneValue = ""
							except:
								QMessageBox.warning(self, "ERROR", "Try Again...")
						elif microphoneValue == 'transpose Matrix two':
							try:
								self.transpose2()
								microphoneValue = ""
							except:
								QMessageBox.warning(self, "ERROR", "Try Again...")
						elif microphoneValue == 'rank Matrix two':
							try:
								self.rank2()
								microphoneValue = ""
							except:
								QMessageBox.warning(self, "ERROR", "Try Again...")
						elif microphoneValue == 'multiply Matrix two':
							try:
								self.mult_scalar2()
								microphoneValue = ""
							except:
								QMessageBox.warning(self, "ERROR", "Try Again...")
						else:
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

	# %% User input connections of the interface
	def inputs(self):
		if self.ui.row_m1.text() != '' or self.ui.column_m1.text() != '':
			try:
				# Getting row number of first matrix from line edit
				self.number_of_rows_matrix1 = int(self.ui.row_m1.text())
				# Getting column number of first matrix from line edit
				self.number_of_columns_matrix1 = int(self.ui.column_m1.text())
				self.matrix1 = [(i, j) for i in range(int(self.ui.column_m1.text())) for j in range(int(self.ui.row_m1.text()))]
			except ValueError:
				pass
		if self.ui.row_m2.text() != '' or self.ui.column_m2.text() != '':
			try:
				self.number_of_rows_matrix2 = int(self.ui.row_m2.text())
				# §self.ui.row_m2.setText(str(int(self.ui.column_m1.text()))) #the number of rows of the second
				# matrix appears as the number of columns of the first according to the matrix multiplication rule

				# Getting row number of first matrix from line edit
				self.number_of_columns_matrix2 = int(self.ui.column_m2.text())
				self.matrix2 = [(i, j) for i in range(int(self.ui.column_m2.text())) for j in range(int(self.ui.row_m2.text()))]
			except ValueError:
				pass

	# %% Visibility.

	def visible1_false(self):
		self.ui.label_6.setVisible(False)
		self.ui.line.setVisible(False)
		self.ui.determinant_btn_1.setVisible(False)
		self.ui.display_det_1.setVisible(False)
		self.ui.inverse_btn_1.setVisible(False)
		self.ui.transpose_btn_1.setVisible(False)
		self.ui.rank_btn_1.setVisible(False)
		self.ui.multiplyby_btn.setVisible(False)
		self.ui.takenumbermult_1.setVisible(False)
		self.ui.rank_1.setVisible(False)

	def visible1_true(self):
		self.ui.label_6.setVisible(True)
		self.ui.line.setVisible(True)
		self.ui.determinant_btn_1.setVisible(True)
		self.ui.display_det_1.setVisible(True)
		self.ui.inverse_btn_1.setVisible(True)
		self.ui.transpose_btn_1.setVisible(True)
		self.ui.rank_btn_1.setVisible(True)
		self.ui.multiplyby_btn.setVisible(True)
		self.ui.takenumbermult_1.setVisible(True)
		self.ui.rank_1.setVisible(True)

	def visible2_false(self):
		self.ui.label_7.setVisible(False)
		self.ui.line_2.setVisible(False)
		self.ui.determinant_btn_2.setVisible(False)
		self.ui.inverse_btn_2.setVisible(False)
		self.ui.transpose_btn_2.setVisible(False)
		self.ui.rank_btn_2.setVisible(False)
		self.ui.multiplyby_btn_2.setVisible(False)
		self.ui.takenumbermult_2.setVisible(False)
		self.ui.rank_2.setVisible(False)
		self.ui.display_det_2.setVisible(False)

	def visible2_true(self):
		self.ui.label_7.setVisible(True)
		self.ui.line_2.setVisible(True)
		self.ui.determinant_btn_2.setVisible(True)
		self.ui.inverse_btn_2.setVisible(True)
		self.ui.transpose_btn_2.setVisible(True)
		self.ui.rank_btn_2.setVisible(True)
		self.ui.multiplyby_btn_2.setVisible(True)
		self.ui.takenumbermult_2.setVisible(True)
		self.ui.rank_2.setVisible(True)
		self.ui.display_det_2.setVisible(True)

	# %% Generate Random Matrices.
	# Creating tables of matrices with the number of rows and columns received from the user and placing the generated random matrices into the table
	def random_matrices(self):
		self.visible1_false()
		self.visible2_false()
		if self.ui.row_m1.text() == '' and self.ui.column_m1.text() == '' and self.ui.row_m2.text() == '' and self.ui.column_m2.text() == '':
			self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")
		else:
			try:
				# setting the row number of the first table as the number of rows received
				self.ui.Matrix_1.setRowCount(int(self.ui.row_m1.text()))
				# setting the column number of the first table as the number of columns received
				self.ui.Matrix_1.setColumnCount(int(self.ui.column_m1.text()))
				# Creating random matrices with the help of a function I called in another file
				self.matrices = create_matrix.randommatrix(int(self.ui.row_m1.text()), int(self.ui.column_m1.text()),
														   int(self.ui.row_m2.text()), int(self.ui.column_m2.text()))
				# Determining the matrix at index 0 as the first matrix among the matrices in the list returned from
				# the function I wrote
				self.matrix1 = self.matrices[0]

				for i, row_1 in enumerate(
						self.matrix1):  # Placing the first random matrix created using the enumerate function into the first table
					for j, val in enumerate(row_1):
						newItem1 = QtWidgets.QTableWidgetItem(str(val))
						newItem1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
						self.ui.Matrix_1.setItem(i, j, newItem1)

				# setting the number of rows of the second matrix as the number of columns of the first matrix
				self.ui.Matrix_2.setRowCount(int(self.ui.row_m2.text()))
				# setting the column number of the second table as the number of columns received
				self.ui.Matrix_2.setColumnCount(int(self.ui.column_m2.text()))
				# Determining the matrix at index 1 as the first matrix among the matrices in the list returned from
				# the function I wrote
				self.matrix2 = self.matrices[1]
				for i in range(int(self.ui.column_m1.text())):
					self.ui.Matrix_1.setColumnWidth(i, 500 / int(self.ui.column_m1.text()))

				for i in range(int(self.ui.row_m1.text())):  # set the row of first matrix height to 50 px
					self.ui.Matrix_1.setRowHeight(i, 300 / int(self.ui.row_m1.text()))

				for i in range(int(self.ui.column_m2.text())):
					self.ui.Matrix_2.setColumnWidth(i, 500 / int(self.ui.column_m2.text()))

				for i in range(int(self.ui.row_m2.text())):  # set the row of second matrix height to 50 px
					self.ui.Matrix_2.setRowHeight(i, 300 / int(self.ui.row_m2.text()))

				for k, row_2 in enumerate(
						self.matrix2):  # Placing the second random matrix created using the enumerate function into the second table
					for l, value in enumerate(row_2):
						newItem2 = QtWidgets.QTableWidgetItem(str(value))
						newItem2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
						self.ui.Matrix_2.setItem(k, l, newItem2)
			except AttributeError:
				self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

	# %%Create Matrix 1
	def matrix1_user(self):
		self.ui.Matrix_1.clear()  # cleaning the table of first matrix
		if self.ui.row_m1.text() == '' or self.ui.column_m1.text() == '':
			# if self.ui.row_m1.text()=='' or self.ui.column_m1.text()=='' and self.ui.row_m2.text()=='' or
			# self.ui.column_m2.text()=='':
			self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")
		else:
			try:
				self.visible1_true()
				# setting the row number of the first table as the number of rows received
				self.ui.Matrix_1.setRowCount(int(self.ui.row_m1.text()))
				# setting the column number of the first table as the number of columns received
				self.ui.Matrix_1.setColumnCount(int(self.ui.column_m1.text()))
				for i in range(int(self.ui.column_m1.text())):
					self.ui.Matrix_1.setColumnWidth(i, 500 / int(self.ui.column_m1.text()))

				for i in range(int(self.ui.row_m1.text())):  # set the row of first matrix height to 50 px
					self.ui.Matrix_1.setRowHeight(i, 300 / int(self.ui.row_m1.text()))
			except AttributeError:
				self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

	# %%Create Matrix 2
	def matrix2_user(self):
		self.ui.Matrix_2.clear()  # cleaning the table of second matrix
		if self.ui.row_m2.text() == '' or self.ui.column_m2.text() == '':
			# if self.ui.row_m1.text()=='' or self.ui.column_m1.text()=='' and self.ui.row_m2.text()=='' or
			# self.ui.column_m2.text()=='':
			self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")
		else:
			try:
				self.visible2_true()
				self.ui.Matrix_2.setRowCount(
					int(self.ui.row_m2.text()))  # setting the number of rows of the second matrix as the number of columns of the first matrix
				self.ui.Matrix_2.setColumnCount(
					int(self.ui.column_m2.text()))  # setting the column number of the second table as the number of columns received
				for i in range(int(self.ui.column_m2.text())):
					self.ui.Matrix_2.setColumnWidth(i, 500 / int(self.ui.column_m2.text()))

				for i in range(int(self.ui.row_m2.text())):  # set the row of second matrix height to 50 px
					self.ui.Matrix_2.setRowHeight(i, 300 / int(self.ui.row_m2.text()))

			except AttributeError:
				self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

	# %%Determinant

	def determinant1(self):
		self.matrix1 = [[(i, j) for i in range(int(self.ui.column_m1.text()))] for j in range(int(self.ui.row_m1.text()))]
		if self.ui.row_m1.text() != self.ui.column_m1.text():
			self.msg = QMessageBox.critical(self, "Error",
											"Last 2 dimensions of the array must be square!"
											"\nPlease check your first matrix row count and column count......")
		else:
			try:
				for i in range(len(self.matrix1)):
					for j in range(len(self.matrix1[0])):
						self.matrix1[i][j] = float(self.ui.Matrix_1.item(i, j).text())

				print(self.matrix1)
				self.matrix1 = np.asarray(self.matrix1)
				self.det = np.linalg.det(self.matrix1)
				self.ui.display_det_1.setText(str(math.ceil(self.det)))
			except ValueError:
				self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
			except AttributeError:
				self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

	def determinant2(self):
		self.matrix2 = [[(i, j) for i in range(int(self.ui.column_m2.text()))] for j in range(int(self.ui.row_m2.text()))]
		if self.ui.row_m2.text() != self.ui.column_m2.text():
			self.msg = QMessageBox.critical(self, "Error",
											"Last 2 dimensions of the array must be square!"
											"\nPlease check your second matrix row count and column count...")
		else:
			try:
				for i in range(len(self.matrix2)):
					for j in range(len(self.matrix2[0])):
						self.matrix2[i][j] = float(self.ui.Matrix_2.item(i, j).text())
				self.matrix2 = np.asarray(self.matrix2)
				self.det2 = np.linalg.det(self.matrix2)
				print("determinant")
				print(self.det)
				self.ui.display_det_2.setText(str(math.ceil(self.det2)))
			except ValueError:
				self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
			except AttributeError:
				self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

	# %%Inverse Matrix
	def inverse1(self):
		if self.ui.row_m1.text() != self.ui.column_m1.text():
			self.msg = QMessageBox.critical(self, "Error",
											"Last 2 dimensions of the array must be square!\nPlease check your first matrix row count and column count......")
		else:
			try:
				for i in range(len(self.matrix1)):
					for j in range(len(self.matrix1[0])):
						self.matrix1[i][j] = float(self.ui.Matrix_1.item(i, j).text())
				self.matrix1 = np.asarray(self.matrix1)
				self.det = np.linalg.det(self.matrix1)
				if self.det != 0:
					self.matrix1 = np.asarray(self.matrix1)
					self.inverse_1 = np.linalg.inv(self.matrix1)
					for i, row_1 in enumerate(
							self.inverse_1):  # Placing the first random matrix created using the enumerate function into the first table
						for j, val in enumerate(row_1):
							newItem1 = QtWidgets.QTableWidgetItem(str(val))
							newItem1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
							self.ui.Matrix_1.setItem(i, j, newItem1)

				else:
					self.msg = QMessageBox.critical(self, "Error",
													"For inverse matrix, determinant must be non-zero...")
			except ValueError:
				self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
			except AttributeError:
				self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

	def inverse2(self):
		if self.ui.row_m2.text() != self.ui.column_m2.text():
			self.msg = QMessageBox.critical(self, "Error",
											"Last 2 dimensions of the array must be square!\nPlease check your first matrix row count and column count......")
		else:
			try:
				for i in range(len(self.matrix2)):
					for j in range(len(self.matrix2[0])):
						self.matrix2[i][j] = float(self.ui.Matrix_2.item(i, j).text())
				self.matrix2 = np.asarray(self.matrix2)
				self.det = np.linalg.det(self.matrix2)
				if self.det != 0:
					self.matrix2 = np.asarray(self.matrix2)
					self.inverse_2 = np.linalg.inv(self.matrix2)
					for k, row_2 in enumerate(
							self.inverse_2):  # Placing the second random matrix created using the enumerate function into the second table
						for l, value in enumerate(row_2):
							newItem2 = QtWidgets.QTableWidgetItem(str(value))
							newItem2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
							self.ui.Matrix_2.setItem(k, l, newItem2)

				else:
					self.msg = QMessageBox.critical(self, "Error",
													"For inverse matrix, determinant must be non-zero...")
			except ValueError:
				self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
			except AttributeError:
				self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

	# %%Transpose Matrix
	def transpose1(self):
		try:
			for i in range(len(self.matrix1)):
				for j in range(len(self.matrix1[0])):
					self.matrix1[i][j] = float(self.ui.Matrix_1.item(i, j).text())
			self.matrix1 = np.asarray(self.matrix1)
			self.matrix1 = self.matrix1.transpose()
			rows = len(self.matrix1)
			columns = len(self.matrix1[0])
			self.ui.Matrix_1.setRowCount(len(self.matrix1))  # cleaning the row value of table of first matrix
			self.ui.Matrix_1.setColumnCount(len(self.matrix1[0]))  # cleaning the column value of table of first matrix
			for i in range(columns):
				self.ui.Matrix_1.setColumnWidth(i, 500 / columns)
			for i in range(rows):  # set the row of second matrix height to 50 px
				self.ui.Matrix_1.setRowHeight(i, 300 / rows)
			for i, row_1 in enumerate(
					self.matrix1):  # Placing the first random matrix created using the enumerate function into the first table
				for j, val in enumerate(row_1):
					newItem1 = QtWidgets.QTableWidgetItem(str(val))
					newItem1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
					self.ui.Matrix_1.setItem(i, j, newItem1)

		except ValueError:
			self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
		except AttributeError:
			self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

	def transpose2(self):
		try:
			for i in range(len(self.matrix2)):
				for j in range(len(self.matrix2[0])):
					self.matrix2[i][j] = float(self.ui.Matrix_2.item(i, j).text())
			self.matrix2 = np.asarray(self.matrix2)
			self.matrix2 = self.matrix2.transpose()
			rows = len(self.matrix2)
			columns = len(self.matrix2[0])
			self.ui.Matrix_2.setRowCount(len(self.matrix2))  # cleaning the row value of table of first matrix
			self.ui.Matrix_2.setColumnCount(len(self.matrix2[0]))  # cleaning the column value of table of first matrix
			for i in range(columns):
				self.ui.Matrix_2.setColumnWidth(i, 500 / columns)

			for i in range(rows):  # set the row of second matrix height to 50 px
				self.ui.Matrix_2.setRowHeight(i, 300 / rows)
			for k, row_2 in enumerate(
					self.matrix2):  # Placing the second random matrix created using the enumerate function into the second table
				for l, value in enumerate(row_2):
					newItem2 = QtWidgets.QTableWidgetItem(str(value))
					newItem2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
					self.ui.Matrix_2.setItem(k, l, newItem2)

		except ValueError:
			self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
		except AttributeError:
			self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

	# %%Rank Matrix
	def rank1(self):
		if self.ui.row_m1.text() != self.ui.column_m1.text():
			self.msg = QMessageBox.critical(self, "Error",
											"Last 2 dimensions of the array must be square!\nPlease check your first "
											"matrix row count and column count......")
		else:
			try:
				for i in range(len(self.matrix1)):
					for j in range(len(self.matrix1[0])):
						self.matrix1[i][j] = float(self.ui.Matrix_1.item(i, j).text())
				self.matrix1 = np.asarray(self.matrix1)
				self.det = np.linalg.det(self.matrix1)
				if self.det != 0:
					self.matrix1 = np.asarray(self.matrix1)
					self.rank_1 = np.linalg.matrix_rank(self.matrix1)
					self.ui.rank_1.setText(str(self.rank_1))
				else:
					self.msg = QMessageBox.critical(self, "Error", "The determinant must be non-zero...")

			except ValueError:
				self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
			except AttributeError:
				self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

	def rank2(self):
		if self.ui.row_m2.text() != self.ui.column_m2.text():
			self.msg = QMessageBox.critical(self, "Error",
											"Last 2 dimensions of the array must be square!\nPlease check your first matrix row count and column count......")
		else:
			try:
				for i in range(len(self.matrix2)):
					for j in range(len(self.matrix2[0])):
						self.matrix2[i][j] = float(self.ui.Matrix_2.item(i, j).text())
				self.matrix2 = np.asarray(self.matrix2)
				self.det = np.linalg.det(self.matrix2)
				if self.det != 0:
					self.matrix2 = np.asarray(self.matrix2)
					self.rank_2 = np.linalg.matrix_rank(self.matrix2)
					self.ui.rank_2.setText(str(self.rank_2))
				else:
					self.msg = QMessageBox.critical(self, "Error", "The determinant must be non-zero...")

			except ValueError:
				self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
			except AttributeError:
				self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

	# %%Multiply by:

	def mult_scalar1(self):
		try:
			if self.ui.takenumbermult_1.text() == '':
				self.msg = QMessageBox.critical(self, "Error", "Please enter a scalar number...")
				self.ui.takenumbermult_1.setStyleSheet("background-color: rgb(255,0,0);\n"
													   "border-radius: 10px ;\n"
													   "border-width: 3px;\n"
													   "border-color: rgb(170,74,48);")
				time.sleep(5)
				self.ui.takenumbermult_1.setStyleSheet("background-color: rgb(255, 212, 169);\n"
													   "border-radius: 10px ;\n"
													   "border-width: 3px;\n"
													   "border-color: rgb(170,74,48);")
			else:
				scalar = int(self.ui.takenumbermult_1.text())
				for i in range(len(self.matrix1)):
					for j in range(len(self.matrix1[0])):
						self.matrix1[i][j] = float(self.ui.Matrix_1.item(i, j).text())
				self.matrix1 = np.asarray(self.matrix1)
				self.new_matrix1 = scalar * self.matrix1
				for k, row_1 in enumerate(
						self.new_matrix1):  # Placing the second random matrix created using the enumerate function into the second table
					for l, value in enumerate(row_1):
						newItem1 = QtWidgets.QTableWidgetItem(str(value))
						newItem1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
						self.ui.Matrix_1.setItem(k, l, newItem1)

		except ValueError:
			self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
		except AttributeError:
			self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

	def mult_scalar2(self):
		try:
			if self.ui.takenumbermult_1.text() == '':
				self.msg = QMessageBox.critical(self, "Error", "Please enter a scalar number...")
			else:
				scalar = int(self.ui.takenumbermult_2.text())
				for i in range(len(self.matrix2)):
					for j in range(len(self.matrix2[0])):
						self.matrix2[i][j] = float(self.ui.Matrix_2.item(i, j).text())
				self.matrix2 = np.asarray(self.matrix2)
				self.new_matrix2 = scalar * self.matrix2
				for k, row_2 in enumerate(
						self.new_matrix2):  # Placing the second random matrix created using the enumerate function into the second table
					for l, value in enumerate(row_2):
						newItem2 = QtWidgets.QTableWidgetItem(str(value))
						newItem2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
						self.ui.Matrix_2.setItem(k, l, newItem2)

		except ValueError:
			self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
		except AttributeError:
			self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

	# %% Matrix Multiplication
	def multiplication(self):
		if self.ui.column_m1.text() != self.ui.row_m2.text():
			self.msg = QMessageBox.critical(self, "Error", "Dimensions not same...")
		else:
			if self.ui.row_m1.text() == '' and self.ui.column_m1.text() == '' and self.ui.row_m2.text() == '' and self.ui.column_m2.text() == '':
				self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")
			else:
				try:
					for i in range(len(self.matrix1)):
						for j in range(len(self.matrix1[0])):
							self.matrix1[i][j] = float(self.ui.Matrix_1.item(i, j).text())
					for i in range(len(self.matrix2)):
						for j in range(len(self.matrix2[0])):
							self.matrix2[i][j] = float(self.ui.Matrix_2.item(i, j).text())
					# Calling the matrix multiplication function I wrote and performing the operation
					self.result_matrix = matrix_mult.multiplication(self.matrix1, self.matrix2)
					self.ui.resultmatrix.setRowCount(
						len(self.result_matrix))  # setting the number of rows of the table where the result matrix will appear
					self.ui.resultmatrix.setColumnCount(len(self.result_matrix[
																0]))  # setting the number of columns of the table where the result matrix will appear

					for i in range(
							len(self.result_matrix[0])):  # change the column width value of the table for result matrix
						self.ui.resultmatrix.setColumnWidth(i, 500 / len(self.result_matrix[0]))
					for i in range(len(self.result_matrix)):
						# change the column width value of the table for result matrix
						self.ui.resultmatrix.setRowHeight(i, 300 / len(self.result_matrix))
					# Placing returned from multiplication function using the enumerate function into the result table
					for i, row in enumerate(self.result_matrix):
						for j, val in enumerate(row):
							newItem3 = QtWidgets.QTableWidgetItem(str(val))
							newItem3.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
							self.ui.resultmatrix.setItem(i, j, newItem3)

				except ValueError:
					self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
				except AttributeError:
					self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

	# %% Clear post-values with clear button
	def clear(self):
		self.matrix1_current = 0
		self.matrix2_current = 0
		self.visible1_false()
		self.visible2_false()
		self.matrix1 = []
		self.matrix2 = []
		self.result_matrix = []

		# Cleaning the table of matrices.
		self.ui.Matrix_1.clear()
		self.ui.Matrix_2.clear()
		self.ui.resultmatrix.clear()
		# Cleaning the column&row value of table of matrices.
		self.ui.Matrix_1.setRowCount(0)
		self.ui.Matrix_1.setColumnCount(0)
		self.ui.Matrix_2.setRowCount(0)
		self.ui.Matrix_2.setColumnCount(0)
		self.ui.resultmatrix.setRowCount(0)
		self.ui.resultmatrix.setColumnCount(0)
		# Clear all row and columns.
		self.ui.row_m1.clear()
		self.ui.column_m1.clear()
		self.ui.row_m2.clear()
		self.ui.column_m2.clear()


# %% Initialization
if __name__ == "__main__":
	app = QApplication([])
	window = MatrixOperation()
	window.show()
	sys.exit(app.exec_())
