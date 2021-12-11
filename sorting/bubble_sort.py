# BUBBLE SORT.A/
# (1) for i = 1 to A:length - 1
# (2)   for j = A:length down to i + 1
# (3)       if A[j] < A[j - 1]
# (4)           exchange A[j] with A[j] - 1"

# Performs bubble sort algorithm.
# It was created on October 5, 2021.

# Written by Orhan Ozan Yildiz.
from sorting.sorter import Sorter


class BubbleSort(Sorter):
	# Sorting algorithm name.
	BUBBLE_SORT = "Bubble Sort"

	def __init__(self, unsorted_array):
		# Calls the parent abstract class constructor (__init__ method).
		super().__init__(unsorted_array)

	# @property decorator; a *pythonic* way to use getters and setters in object-oriented programming.
	@property
	# getter method.
	def get_algorithm_name(self):
		return BubbleSort.BUBBLE_SORT

	def sorting(self):
		BubbleSort.bubble_sort(self.unsorted_array)

	# *A class method takes cls as the first parameter while a static method needs no specific parameters.
	# *A class method can access or modify the class state while a static method can't access or modify it.
	# *In general, static methods know nothing about the class state.
	# They are utility-type methods that take some parameters and work upon those parameters.
	# We generally use static method to create utility functions. Such as bubble sort, merge sort algorithms.
	@staticmethod
	def bubble_sort(sorting_array):
		# Cycles through all array elements.
		operations = 0
		for i in range(len(sorting_array) - 1):
			operations += 1
			for j in range(len(sorting_array) - 1 - i):
				if sorting_array[j] > sorting_array[j + 1]:
					# If the element is greater than its adjacent value, replace it.
					sorting_array[j], sorting_array[j + 1] = sorting_array[j + 1], sorting_array[j]
		return operations
