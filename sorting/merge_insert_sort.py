# MERGE INSERTION SORT
# (1) If n = 1, done
# (2) Recursively sort A[1..⌈n/2⌉] and A[⌈n/2⌉+1..n].
# (3) "Merge" the 2 sorted lists.

# Performs merge based insertion sorting algorithm.
# It was created on October 5, 2021.

# Written by Orhan Ozan Yildiz.
from sorting.insertion_sort import InsertionSort
from sorting.merge_sort import MergeSort
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

		first_half = InsertionSort.insertion_sort(start_half)
		second_half = InsertionSort.insertion_sort(end_half)

		MergeSort.merge(unsorted_array, first_half, second_half)
