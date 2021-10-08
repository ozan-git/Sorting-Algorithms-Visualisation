# Perform insertion, bubble and merge sorting algorithms.
# 5 October 2021.

# Written by Orhan Ozan Yildiz.

import sortingAlgorithms


def calling_sorting(unsorted_array):
	print(unsorted_array)

	# Calling insertion sort functions.
	insertion_list = sortingAlgorithms.insertion_sort(unsorted_array)
	print(insertion_list)

	# Calling bubble sort functions.
	bubble_list = sortingAlgorithms.bubble_sort(unsorted_array)
	print(bubble_list)

	# Calling merge sort functions.
	merge_list = sortingAlgorithms.SortAlgorithm().merge_sort(unsorted_array, 0, (len(unsorted_array) - 1))
	print(merge_list)


print("""
Press 1 if you want to use a random array,
press 2 if you want to decide the array, and
press 9 if you want to exit.
""")

flag = True
while flag:
	try:
		chosenInput = int(input("please select one: "))
		# Using random array.
		if chosenInput == 1:
			array = sortingAlgorithms.random_array()
			print("Random array is:")

			# Calling sorting functions.
			calling_sorting(array)

			print(sortingAlgorithms.time_sort())
		elif chosenInput == 2:
			arr = sortingAlgorithms.user_array()

			print("User array is:")

			# Calling sorting functions.
			calling_sorting(arr)

			print(sortingAlgorithms.time_sort())
		elif chosenInput == 9:
			break
		else:
			print("This input not valid. Please try again.")
	except ValueError:
		print("This input not valid. Please try again.")
