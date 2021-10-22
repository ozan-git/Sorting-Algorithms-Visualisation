# MERGE(A, p, q, r)
# (1) n1 = q - p + 1
# (2) n2 = r - q
# (3) let L[1..n1 +1] and R[1..n2 + 1] be new arrays
# (4) for i = 1 to n1
# (5)   L[i] = A[p + i - 1]
# (6) for j = 1 to n2
# (7)   R[j] = A[q + j]
# (8) L[n1 + 1] = 1
# (9) R[n2 + 1] = 1
# (10) i = 1
# (11) j = 1
# (12) for k = p to r
# (13)  if L[i] <= R[j]
# (14)      A[k] D L[i]
# (15)      i = i + 1
# (16)  else A[k] = R[j]
# (17)      j = j + 1

# Performs bubble sort algorithm.
# It was created on October 5, 2021.

# Written by Orhan Ozan Yildiz.

from sorting.sorter import Sorter


class MergeSort(Sorter):
	# Sorting algorithm name.
	MERGE_SORT = "Merge Sort"

	def __init__(self, unsorted_array):
		# Calls the parent abstract class constructor (__init__ method).
		super().__init__(unsorted_array)

	# @property decorator; a *pythonic* way to use getters and setters in object-oriented programming.
	@property
	# getter method.
	def get_algorithm_name(self):
		return MergeSort.MERGE_SORT

	def sorting(self):
		MergeSort.merge_sort(self.unsorted_array)

	# p is start point and r is end point.
	@staticmethod
	# mergeSort is merge sort function.
	# A is array, p is start point and r is end point.
	def merge_sort(unsorted_array):
		# Base condition.
		if len(unsorted_array) < 2:
			return
		# Find the mid index.
		mid = int(len(unsorted_array) / 2)
		start_half = unsorted_array[0: mid]
		end_half = unsorted_array[mid: len(unsorted_array)]

		MergeSort.merge_sort(start_half)
		MergeSort.merge_sort(end_half)
		MergeSort.merge(unsorted_array, start_half, end_half)

	@staticmethod
	def merge(double_list, start_half, end_half):
		i, j, k = 0, 0, 0
		length_part_left, length_part_right = len(start_half), len(end_half)

		while i < len(start_half) and j < length_part_right:
			if start_half[i] >= end_half[j]:
				double_list[k] = end_half[j]
				k, j = (k + 1), (j + 1)
			else:
				double_list[k] = start_half[i]
				k, i = (k + 1), (i + 1)

		while i < len(start_half):
			double_list[k] = start_half[i]
			k, i = (k + 1), (i + 1)

		while j < length_part_right:
			double_list[k] = end_half[j]
			k, j = (k + 1), (j + 1)
