# INSERTION SORT
# (1) for j = 2 to A.length
# (2)     key = A[j]
# (3)     // Insert A[j] into the sorted sequence A[1..j - 1].
# (4)     i = j - 1
# (5)     while i > 0 and A[i] and A[i] > key
# (6)         A[i + 1] = A[i]
# (7)         i = i - 1
# (8)     A[i + 1] = key

# Performs insertion sort algorithm.
# It was created on October 5, 2021.

# Written by Orhan Ozan Yildiz.
from sorting.sorter import Sorter


class InsertionSort(Sorter):
	# Sorting algorithm name.
	INSERTION_SORT = "Insertion Sort"

	def __init__(self, unsorted_array):
		# Calls the parent abstract class constructor (__init__ method).
		super().__init__(unsorted_array)

	# @property decorator; a *pythonic* way to use getters and setters in object-oriented programming.
	@property
	# getter method.
	def get_algorithm_name(self):
		return InsertionSort.INSERTION_SORT

	def sorting(self):
		InsertionSort.insertion_sort(self.unsorted_array)

	@staticmethod
	def insertion_sort(unsorted_array):
		# (1) for j(iterationNumber) = 2 to A(array).length.
		# Our array index started from 0, so we need to take j = 1.
		for iterationNumber in range(1, len(unsorted_array)):
			# (2) key = A[j].
			key = unsorted_array[iterationNumber]

			# (3) and (4) Insert A[j] into the sorted sequence A[1..j - 1].
			j = iterationNumber - 1
			# (5), (6), (7) and (8).
			while j >= 0 and unsorted_array[j] > key:
				unsorted_array[j + 1] = unsorted_array[j]
				j -= 1
			unsorted_array[j + 1] = key
		return unsorted_array
