# Perform insertion, bubble and merge sorting algorithms.
# 5 October 2021.

# Written by Orhan Ozan Yildiz.
import random
import time

import matplotlib.pyplot as plt
from numpy.random import seed, randint

from sorting.bubble_sort import BubbleSort
from sorting.insertion_sort import InsertionSort
from sorting.merge_insert_sort import MergeInsertionSort
from sorting.merge_sort import MergeSort

# assuming we are in Jupyter:
# Initialize of result for compare the computational time with respect to n (number of inputs).
insertion_comp_time = []
bubble_comp_time = []
merge_comp_time = []
merge_insertion_comp_time = []


# Generating a random array based on user inputs.
def generate_random_array():
	generated_array = []
	size_array = int(input("How many numbers should the array consist of: "))
	i_min = int(input("What is the smallest value: "))
	i_max = int(input("What is the largest value: "))
	for iteration in range(size_array):
		# Creating random array.
		values = random.randint(i_min, i_max)
		# The resulting random values are added to the array.
		generated_array.append(int(values))
	return generated_array


# This function is used to test the entered values.
def check_entered_values():
	user_input = input()
	while True:
		try:
			if user_input == "ok":
				break
			float(user_input)
			break
		except ValueError:
			print("Value error. Try again.")
			user_input = input()
	return user_input


# The analysis of the sorting algorithms with respect to array size.
def analyse_sorting_algorithms(array_to_be_sorted):
	start_time = time.time()
	array_to_be_sorted.sorting()
	end_time = time.time()

	# The elapsed time is recorded.
	computational_time = end_time - start_time

	# Store execution times.
	algorithm_name = array_to_be_sorted.get_algorithm_name
	if algorithm_name == InsertionSort.INSERTION_SORT:
		insertion_comp_time.append(computational_time)
	elif algorithm_name == MergeInsertionSort.MERGE_INSERTION_SORT:
		merge_insertion_comp_time.append(computational_time)
	elif algorithm_name == MergeSort.MERGE_SORT:
		merge_comp_time.append(computational_time)
	elif algorithm_name == BubbleSort.BUBBLE_SORT:
		bubble_comp_time.append(computational_time)

	print(
		array_to_be_sorted.get_algorithm_name + " computational time with respect to size of array is " + str(
			computational_time))


# The menu will first ask whether to enter the array manually or to create it randomly.
# Afterwards, the user is asked which sorting method they want to sort with, and the user can compare these tests
# or exit the application.
infinity_loop = True


def ask_operation_fun():
	operation = input("""
Press 1 Insertion sort,
press 2 Merge sort based on insertion sort,
press 3 Merge sort,
press 4 Bubble sort, or
press 5 Exit.
Enter value: """)
	return operation


def operate_sorting_fun(uns_array):
	# Insertion sort.
	if chosen_operation == str(1):
		sorter = InsertionSort(uns_array)
		sorter.sorting()
		print("Sorted array by using insertion sort: \n" + str(sorter.unsorted_array))

	# Merge sort based on insertion sort.
	elif chosen_operation == str(2):
		sorter = MergeInsertionSort(uns_array)
		sorter.sorting()
		print("Sorted array by using merge based insertion sort: \n" + str(sorter.unsorted_array))

	# Merge sort.
	elif chosen_operation == str(3):
		sorter = MergeSort(uns_array)
		sorter.sorting()
		print("Sorted array by using merge sort: \n" + str(sorter.unsorted_array))

	# Bubble sort.
	elif chosen_operation == str(4):
		sorter = BubbleSort(uns_array)
		sorter.sorting()
		print("Sorted array by using bubble sort: \n" + str(sorter.unsorted_array))


while infinity_loop:
	try:
		select_process = input("""
Press 1 if you want to use a random array,
press 2 if you want to decide the array,
press 3 if you want to compare sorting algorithms, or
press 4 if you want to exit.
Enter Value: """)
		# Using random array.
		if select_process == str(1):
			chosen_operation = ask_operation_fun()

			if chosen_operation == str(5):
				infinity_loop = False

			elif chosen_operation == str(1) or chosen_operation == str(2) or chosen_operation == str(
					3) or chosen_operation == str(4):
				rand_array = generate_random_array()
				print("Random array is:")
				print(rand_array)

				operate_sorting_fun(rand_array)

		# Using manual array.
		elif select_process == str(2):
			chosen_operation = ask_operation_fun()

			if chosen_operation == str(5):
				infinity_loop = False

			elif chosen_operation == str(1) or chosen_operation == str(2) or chosen_operation == str(
					3) or chosen_operation == str(4):
				unsorted_array = []
				element = input("Please enter numbers using commas: ")
				array_elements = element.split(",")
				for i in array_elements:
					unsorted_array.append(int(i))

				operate_sorting_fun(unsorted_array)

		# Compare the computational time with respect to n (number of inputs).
		elif select_process == str(3):
			different_array_sizes = [10, 25, 50, 100, 200, 300, 600, 800, 1000, 2000, 3000, 4000, 5000]

			insertion_comp_time.clear()
			merge_comp_time.clear()
			merge_insertion_comp_time.clear()
			bubble_comp_time.clear()

			for array_size in different_array_sizes:
				seed(1)
				insertion_sort = InsertionSort(randint(low=1, high=array_size, size=array_size))
				merge_insertion_sort = MergeInsertionSort(randint(1, array_size, array_size))
				merge_sort = MergeSort(randint(1, array_size, array_size))
				bubble_sort = BubbleSort(randint(1, array_size, array_size))

				print("\n\nArray size: " + str(array_size) + "\n")
				analyse_sorting_algorithms(insertion_sort)
				analyse_sorting_algorithms(merge_insertion_sort)
				analyse_sorting_algorithms(merge_sort)
				analyse_sorting_algorithms(bubble_sort)

			plt.xlabel('List Length')
			plt.ylabel('Time Complexity')
			plt.plot(different_array_sizes, insertion_comp_time, label='Insertion Sort')
			plt.plot(different_array_sizes, merge_comp_time, label='Merge Sort')
			plt.plot(different_array_sizes, merge_insertion_comp_time, label='Merge-Insertion Sort')
			plt.plot(different_array_sizes, bubble_comp_time, label='Bubble Sort')
			plt.grid()
			plt.legend()
			plt.show()

		# Exit.
		elif select_process == str(4):
			break
		else:
			print("This input not valid. Please choose 1, 2, 3 or 4.")
	except ValueError:
		print("This input not valid. Please try again.")
