# MERGE INSERTION SORT
# (1) If n = 1, done
# (2) Recursively sort A[1..⌈n/2⌉] and A[⌈n/2⌉+1..n].
# (3) "Merge" the 2 sorted lists.

# Performs merge based insertion sorting algorithm.
# It was created on October 5, 2021.

# Written by Orhan Ozan Yildiz.
from sorting.insertion_sort import InsertionSort
from sorting.sorter import Sorter


class MergeInsertionSort(Sorter):
	# Sorting algorithm name.
	MERGE_INSERTION_SORT = "Merge Insertion Sort"

	def __init__(self, unsorted_array):
		# Calls the parent abstract class constructor (__init__ method).
		super().__init__(unsorted_array)

	@property
	def get_algorithm_name(self):
		return MergeInsertionSort.MERGE_INSERTION_SORT

	def sorting(self):
		MergeInsertionSort.merge_insertion_sort(self.unsorted_array)

	@staticmethod
	def merge_insertion_sort(unsorted_array):
		# Length of the array stored. Pre-calculated instead of multiple calls.
		length_unsorted_array = len(unsorted_array)

		if length_unsorted_array < 2:
			return

		# mid index.
		mid = int(length_unsorted_array / 2)

		start_half = unsorted_array[0: mid]
		end_half = unsorted_array[mid: length_unsorted_array]

		InsertionSort.insertion_sort(start_half)
		InsertionSort.insertion_sort(end_half)

		MergeInsertionSort.merge(unsorted_array, start_half, end_half)

	@staticmethod
	def merge(unsorted_array, start_half, end_half):
		i, j, k = 0, 0, 0
		length_part_left, length_part_right = len(start_half), len(end_half)

		while i < length_part_left and j < length_part_right:
			if start_half[i] < end_half[j]:
				unsorted_array[k] = start_half[i]
				k, i = (k + 1), (i + 1)
			else:
				unsorted_array[k] = end_half[j]
				k, j = (k + 1), (j + 1)

		while i < length_part_left:
			unsorted_array[k] = start_half[i]
			k, i = (k + 1), (i + 1)

		while j < length_part_right:
			unsorted_array[k] = end_half[j]
			k, j = (k + 1), (j + 1)
