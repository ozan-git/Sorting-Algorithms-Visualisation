# Performs quick sort algorithm.
# Quick sort algorithm, like merge sort, applies the dive-and-conquer paradigm.
# Divide: Partition the array Array[p..r] into two (possibly empty) subarray Array[p..(q-1)] and Array[(q+1)..r]
# such that each element of Array[p..(q-1)] is less than or equal to Array[q], which is, in turn, less than or
# equal to each element of Array[(q+1)..r]. Compute the index q as part of this partitioning procedure.
# Conquer: Sort the two subarray Array[p..(q-1)] and Array[(q+1)..r] by recursive calls to quicksort.
# Combine: Because the subarray are already sorted, no work is needed to combine them: the entire array Array[p..r]
# is now sorted.
# It was created on October 22, 2021.
# page 170, CLRS
# Written by Orhan Ozan Yildiz.
from sorting.sorter import Sorter


class QuickSort(Sorter):
	# Sorting algorithm name.
	QUICK_SORT = "Quick Sort"

	def __init__(self, unsorted_array, low, high):
		# Calls the parent abstract class constructor (__init__ method).
		super().__init__(unsorted_array)
		self.low = low
		self.high = high

	# @property decorator; a *pythonic* way to use getters and setters in object-oriented programming.
	@property
	# getter method.
	def get_algorithm_name(self):
		return QuickSort.QUICK_SORT

	def sorting(self):
		self.quick_sort(self.unsorted_array, self.low, self.high)

	# PARTITION(Array, p, r)
	# (1) x = Array(r)
	# (2) i = p - 1
	# (3) for j = p to r - 1
	# (4)     if Array[j] <= x
	# (5) 	      i += 1
	# (6)        exchange Array[i] with Array[j]
	# (7) exchange Array[i+1] with Array[r]
	# (8) return i + 1
	@staticmethod
	def partition(unsorted_array, low, high):
		index_small = low - 1
		pivot = unsorted_array[high]
		for j in range(low, high):
			if unsorted_array[j] <= pivot:
				index_small += 1
				unsorted_array[index_small], unsorted_array[j] = unsorted_array[j], unsorted_array[index_small]
		unsorted_array[index_small + 1], unsorted_array[high] = unsorted_array[high], unsorted_array[index_small + 1]
		return index_small + 1

	# QUICKSORT(Array, p, r)
	# (1) if p < r
	# (2)     q = PARTITION(Array, p, r)
	# (3)     QUICKSORT(Array, p, (q-1))
	# (4)     QUICKSORT(Array, (q+1), r)
	@staticmethod
	def quick_sort(unsorted_array, low, high):
		if len(unsorted_array) == 1:
			return unsorted_array

		if low < high:
			q = QuickSort.partition(unsorted_array, low, high)

			QuickSort.quick_sort(unsorted_array, low, q - 1)
			QuickSort.quick_sort(unsorted_array, q + 1, high)
