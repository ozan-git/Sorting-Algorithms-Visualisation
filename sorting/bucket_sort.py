# Performs bucket sort algorithm.
# It was created on October 30, 2021.
# page 200, CLRS
# Written by Orhan Ozan Yildiz.
from sorting.sorter import Sorter


def insertion_sort(bucket):
	for i in range(1, len(bucket)):
		var = bucket[i]
		j = i - 1
		while j >= 0 and var < bucket[j]:
			bucket[j + 1] = bucket[j]
			j = j - 1
		bucket[j + 1] = var


class BucketSort(Sorter):
	# Sorting algorithm name.
	BUCKET_SORT = "Bucket Sort"

	def __init__(self, unsorted_array):
		# Calls the parent abstract class constructor (__init__ method).
		super().__init__(unsorted_array)

	# @property decorator; a *pythonic* way to use getters and setters in object-oriented programming.
	@property
	# getter method.
	def get_algorithm_name(self):
		return BucketSort.BUCKET_SORT

	def sorting(self):
		BucketSort.bucket_sort(self.unsorted_array)

	# BUCKET-SORT(A)
	# (1) let B[0..n-1] be a new array
	# (2) n = A.length
	# (3) for i = 0 to n - 1
	# (4)     make B[i] an empty list
	# (5) for i = 1 to n
	# (6)     insert A[i] into list B [⌊nA[i]⌋]
	# (7) for i = 0 to n - 1
	# (8)     sort list B[i] with insertion sort
	# (9) concatenate the list B[0],B[1],...B[n-1] together in order
	@staticmethod
	def bucket_sort(unsorted_array):
		# (1) (2) Find maximum value in the list and use length of the list to determine which value in the
		# list goes into which bucket.
		max_value = max(unsorted_array)
		size = max_value / len(unsorted_array)
		# Create n empty buckets where n is equal to the length of the input list.
		bucket = []
		for i in range(len(unsorted_array)):
			bucket.append([])

		# Put array elements in different buckets
		for i in range(len(unsorted_array)):
			j = int(unsorted_array[i] / size)
			if j != len(unsorted_array):
				bucket[j].append(unsorted_array[i])
			else:
				bucket[len(unsorted_array) - 1].append(unsorted_array[i])

		# Sort individual buckets
		for i in range(len(unsorted_array)):
			insertion_sort(bucket[i])

		# concatenate the result
		result = []
		for i in range(len(unsorted_array)):
			result += bucket[i]

		for i in range(len(result)):
			unsorted_array[i] = result[i]


# # (1) (2) (3) (4) let B[0..n-1] be a new array
# bucket = []
# for i in range(10):
# 	bucket.append([])
#
# # (5) (6) Put array elements in different elements
# for i in unsorted_array:
# 	index_b = int(10 * i)
# 	bucket[index_b].append(i)
#
# # (7) (8) Sort individual buckets
# for i in range(10):
# 	bucket[i] = sorting.insertion_sort.InsertionSort(bucket[i]).sorting()
#
# # (9) Concatenate the result
# k = 0
# for i in range(len(unsorted_array)):
# 	for j in range(len(bucket[i])):
# 		unsorted_array[k] = bucket[i][j]
# 		k += 1
# return unsorted_array
