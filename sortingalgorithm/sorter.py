# Abstract base class.
# It was created on October 5, 2021.

# Written by Orhan Ozan Yildiz.
from abc import ABC, abstractmethod


# Abstract base class for sortingalgorithm algorithms.
# This class defines methods for subclasses.
class Sorter(ABC):

	def __init__(self, unsorted_array):
		# The array to be sorted.
		self.unsorted_array = unsorted_array

	# Using *abstractmethod* decorator requires that the class's metaclass is ABCMeta or derived from it.
	@abstractmethod
	def get_algorithm_name(self):
		pass

	@abstractmethod
	def sorting(self):
		pass
