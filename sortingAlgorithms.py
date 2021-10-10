# Perform insertion, bubble and merge sorting algorithms.
# 5 October 2021.

# Written by Orhan Ozan Yildiz.

import datetime
import random


# # Generating a random array based on user inputs.
# def random_array():
# 	array = []
# 	size_array = int(input("How many numbers should the array consist of: "))
# 	i_min = int(input("What is the smallest value: "))
# 	iMax = int(input("What is the largest value: "))
# 	for i in range(size_array):
# 		# Creating random array.
# 		values = random.randint(i_min, iMax)
# 		# The resulting random values are added to the array.
# 		array.append(int(values))
# 	return array


# The user creates the array.
def user_array():
	array = []
	element = input("Please enter numbers using commas: ")
	array_elements = element.split(",")
	for i in array_elements:
		array.append(int(i))
	return array


class InputArray:
	def __init__(self):
		pass


# # BUBBLE SORT.A/
# # (1) for i = 1 to A:length - 1
# # (2)   for j = A:length down to i + 1
# # (3)       if A[j] < A[j - 1]
# # (4)           exchange A[j] with A[j] - 1"
# def bubble_sort(array):
# 	# Cycles through all array elements.
# 	for i in range(len(array) - 1):
# 		for j in range(len(array) - 1 - i):
# 			if array[j] > array[j + 1]:
# 				# If the element is greater than its adjacent value, replace it.
# 				array[j], array[j + 1] = array[j + 1], array[j]
# 	return array


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
def merge_sort(array, p, q, r):
	firstHalf = q - p + 1  # First half of array is arr[p..q].
	secondHalf = r - q  # Second half of array is arr[q+1..r].

	left_side = [0] * firstHalf
	right_side = [0] * secondHalf

	# Data is copied to temporary array.
	for i in range(0, firstHalf):
		left_side[i] = array[p + i]

	# Data is copied to temporary array.
	for j in range(0, secondHalf):
		right_side[j] = array[q + 1 + j]

	i = 0  # First half of array.
	j = 0  # Second half of array.
	k = p  # Combining the first and last half.

	while i < firstHalf and j < secondHalf:
		if left_side[i] <= right_side[j]:
			array[k] = left_side[i]
			i += 1
		else:
			array[k] = right_side[j]
			j += 1
		k += 1

	while i < firstHalf:
		# Those to the left of the items in the left half are copied.
		array[k] = left_side[i]
		i += 1
		k += 1

	while j < secondHalf:
		# Items to the right of the items in the left half are copied.
		array[k] = right_side[j]
		j += 1
		k += 1


# (1) for j = 2 to A.length
# (2)     key = A[j]
# (3)     // Insert A[j] into the sorted sequence A[1..j - 1].
# (4)     i = j - 1
# (5)     while i > 0 and A[i] and A[i] > key
# (6)         A[i + 1] = A[i]
# (7)         i = i - 1
# (8)     A[i + 1] = key
# def insertion_sort(array):
# 	# (1) for j(iterationNumber) = 2 to A(array).length.
# 	# Our array index started from 0 so we need to take j = 1.
# 	for iterationNumber in range(1, len(array)):
# 		# (2) key = A[j].
# 		key = array[iterationNumber]
#
# 		# (3) and (4) Insert A[j] into the sorted sequence A[1..j - 1].
# 		j = iterationNumber - 1
# 		# (5), (6), (7) and (8).
# 		while j >= 0 and array[j] > key:
# 			array[j + 1] = array[j]
# 			j -= 1
# 		array[j + 1] = key
# 	return array


class SortAlgorithm:

	def __init__(self):
		pass

	def merge_sort(self, array, p, r):
		if p < r:
			# Same as (p+r) /2, but avoids overflow for large p and r.
			q = (p + (r - 1)) // 2
			self.merge_sort(array, p, q)
			self.merge_sort(array, q + 1, r)
			merge_sort(array, p, q, r)
		return array


def time_sort():
	array = []
	array1 = []
	array2 = []

	for i in range(10):  # For 10 elements.
		values = random.randint(0, 10000)
		array.append(int(values))

	for j in range(1000):  # For 1000 elements.
		values = random.randint(0, 10000)
		array1.append(int(values))

	for k in range(5000):  # For 5000 elements.
		values = random.randint(0, 10000)
		array2.append(int(values))

	# Create empty arrays.
	insertion_array = []
	bubble_array = []
	merge_array = []
	general_array = [array, array1, array2]

	for iteration in general_array:
		init_time_insertion = datetime.datetime.now()  # import datetime
		insertion_sort(iteration)
		last_time_insertion = datetime.datetime.now()
		difference_time_insertion = last_time_insertion - init_time_insertion
		insertion_array.append(difference_time_insertion.seconds + (difference_time_insertion.microseconds / 1000000))

		init_time_bubble = datetime.datetime.now()
		bubble_sort(iteration)
		last_time_bubble = datetime.datetime.now()
		difference_time_bubble = last_time_bubble - init_time_bubble
		bubble_array.append(difference_time_bubble.seconds + (difference_time_bubble.microseconds / 1000000))

		init_time_merge = datetime.datetime.now()
		SortAlgorithm().merge_sort(iteration, 0, len(iteration) - 1)
		last_time_merge = datetime.datetime.now()
		difference_time_merge = last_time_merge - init_time_merge
		merge_array.append(difference_time_merge.seconds + (difference_time_merge.microseconds / 1000000))

	print("insertion_array", insertion_array)
	print("bubble_array", bubble_array)
	print("merge_array", merge_array)


class TimingSort:
	def __init__(self):
		pass
