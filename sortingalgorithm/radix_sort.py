# It was created on October 25, 2021.
# page 191, CLRS
# Written by Orhan Ozan Yildiz.
from sortingalgorithm.sorter import Sorter

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
    def radix_sort(unsorted_array):
        # Find the maximum number to know number of digits
        max1 = max(unsorted_array)

        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1
        while max1 / exp > 0:
