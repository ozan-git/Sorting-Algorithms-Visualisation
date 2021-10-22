# Performs heap sort algorithm.

# It was created on October 22, 2021.
# page 160, CLRS
# Written by Orhan Ozan Yildiz.
from sorting.sorter import Sorter


class HeapSort(Sorter):
	# Sorting algorithm name.
	HEAP_SORT = "Heap Sort"

	def __init__(self, unsorted_array):
		# Calls the parent abstract class constructor (__init__ method).
		super().__init__(unsorted_array)

	# @property decorator; a *pythonic* way to use getters and setters in object-oriented programming.
	@property
	# getter method.
	def get_algorithm_name(self):
		return HeapSort.HEAP_SORT

	def sorting(self):
		HeapSort.heap_sort(self.unsorted_array)

	# HeapSort(A)
	# (1) Build-Max-Heap(A)
	# (2) for i = A.length downto 2
	# (3)     exchange A[1] with A[i]
	# (4)     A.heap-size = A.heap-size - 1
	# (5)     Max-Heapify(A,size_heap,1)
	@staticmethod
	def heap_sort(unsorted_array):
		# n is array length.
		n = len(unsorted_array)

		HeapSort.build_max_hap(unsorted_array)

		for i in range(n - 1, 0, -1):
			unsorted_array[i], unsorted_array[0] = unsorted_array[0], unsorted_array[i]
			HeapSort.heapify(unsorted_array, i, 0)

	# Max-Heapify(A,i)
	# (1) l = LEFT(i)
	# (2) r = RIGHT(i)
	# (3) if l <= A.heap-size and A[l] > A[i]
	# (4)     largest = l
	# (5) else largest = i
	# (6) if r <= A.heap-size and A[r] > A[largest]
	# (7)     largest = r
	# (8) if largest != i
	# (9)     exchange A[i] with A[largest]
	# (10)    Max-Heapify(A, largest)
	@staticmethod
	def heapify(unsorted_array, size_heap, i):
		largest = i
		# left = 2 * i + 1 and right = 2 * i + 2
		left = 2 * i + 1
		right = 2 * i + 2

		if left < size_heap and unsorted_array[i] < unsorted_array[left]:
			largest = left
		if right < size_heap and unsorted_array[right] > unsorted_array[largest]:
			largest = right
		if largest != i:
			unsorted_array[i], unsorted_array[largest] = unsorted_array[largest], unsorted_array[i]

			HeapSort.heapify(unsorted_array, size_heap, largest)

	# Build-Max-Heap(A)
	# (1) A.heap-size = A.length
	# (2) for i = ⌊A.length/2⌋ down to 1
	# (3)     Max-Heapify(A,i)
	@staticmethod
	def build_max_hap(unsorted_array):
		size_array = len(unsorted_array)
		for i in range(size_array // 2 - 1, -1, -1):
			HeapSort.heapify(unsorted_array, size_array, i)
