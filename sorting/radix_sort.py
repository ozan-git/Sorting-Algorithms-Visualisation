# It was created on October 25, 2021.
# page 191, CLRS
# Written by Orhan Ozan Yildiz.
from sorting.sorter import Sorter


class RadixSort(Sorter):
    # Sorting algorithm name.
    RADIX_SORT = "Radix Sort"

    def __init__(self, unsorted_array):
        # Calls the parent abstract class constructor (__init__ method).
        super().__init__(unsorted_array)

    # @property decorator; a *pythonic* way to use getters and setters in object-oriented programming.
    @property
    # getter method.
    def get_algorithm_name(self):
        return RadixSort.RADIX_SORT

    def sorting(self):
        RadixSort.radix_sort(self.unsorted_array)

    @staticmethod
    def counting_sort(unsorted_array, exp1):
        size = len(unsorted_array)
        output = [0] * size

        # Initialize count array
        count = [0] * 10

        # Store the count of each elements in count array
        for i in range(0, size):
            index = unsorted_array[i] // exp1
            count[int(index % 10)] += 1

        # Store the cumulative count
        for i in range(1, 10):
            count[i] = count[i] + count[i - 1]

        # Find the index of each element of the original array in count array
        # place the elements in output array
        for i in range(size - 1, -1, -1):
            index = unsorted_array[i] // exp1
            output[count[int(index % 10)] - 1] = unsorted_array[i]
            count[int(index % 10)] -= 1

        # Copy the sorted elements into original array
        for i in range(0, size):
            unsorted_array[i] = output[i]

    # RADIX-Sort(A,d)
    # (1) for i = 1 to d
    # (2)     use a stable sort to sort array A on digit i
    @staticmethod
    def radix_sort(unsorted_array):
        # Find the maximum number to know number of digits
        max1 = max(unsorted_array)

        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1
        while max1 // exp > 0:
            RadixSort.counting_sort(unsorted_array, exp)
            exp *= 10
