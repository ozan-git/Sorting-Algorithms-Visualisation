# It was created on October 25, 2021.
# page 191, CLRS
# Written by Orhan Ozan Yildiz.

from sorting.sorter import Sorter


class CountingSort(Sorter):
	# Sorting algorithm name.
	COUNTING_SORT = "Counting Sort"

	def __init__(self, unsorted_array):
		# Calls the parent abstract class constructor (__init__ method).
		super().__init__(unsorted_array)

	# @property decorator; a *pythonic* way to use getters and setters in object-oriented programming.
	@property
	# getter method.
	def get_algorithm_name(self):
		return CountingSort.COUNTING_SORT

	def sorting(self):
		CountingSort.counting_sort(self.unsorted_array)

	# COUNTING-SORT(A,B,k)
	#  (1) let C[0..k] be a new array
	#  (2) for i = 0 to k
	#  (3)     C[i] = 0
	#  (4) for j = 1 to A.length
	#  (5)     C[A[j]] = C[A[j]] + 1
	#  (6) // C[i] now contains the number of elements equal to i.
	#  (7) for i = 1 to k
	#  (8)     C[i] = C[i] + C[i - 1]
	#  (9) // C[i] now contains the number of elements less than or equal to i.
	# (10) for j = A.length down to 1
	# (11)    B[C[A[j]]] = A[j]
	# (12)    C[A[j]] = C[A[j]] - 1
	@staticmethod
	def counting_sort(unsorted_array):
		size = len(unsorted_array)
		max_element = int(max(unsorted_array))
		min_element = int(min(unsorted_array))
		range_of_elements = max_element - min_element + 1

		output = [0 for _ in range(size)]
		# Initialize count array.
		count = [0 for _ in range(range_of_elements)]

		# Store the count of each element in count array.
		for i in range(0, size):
			count[unsorted_array[i] - min_element] += 1

		# Store the cumulative count.
		for i in range(1, len(count)):
			count[i] += count[i - 1]

		# Find the index of each element of the original array in count array.
		# Place the elements in output array.
		for i in range(size - 1, -1, -1):
			output[count[unsorted_array[i] - min_element] - 1] = unsorted_array[i]
			count[unsorted_array[i] - min_element] -= 1

		# Copy the sorted elements into original array
		for i in range(0, size):
			unsorted_array[i] = output[i]

		return unsorted_array
