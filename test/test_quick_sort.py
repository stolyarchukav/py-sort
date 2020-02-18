import unittest

from utils.measure import *
from algorithms.quick_sort import *


class QuickSortTest(unittest.TestCase):

    def setUp(self):
        self.__measure = CountMeasure()
        self.__sort = QuickSort(self.__measure)

    def testSort(self):
        source_array = [10, 4, 7, 4, 5]
        sorted_array = self.__sort.sort(source_array)
        self.assertEqual([4, 4, 5, 7, 10], sorted_array)
        self.assertEqual(11, self.__measure.get_count())

    def testSortOrdered(self):
        source_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sorted_array = self.__sort.sort(source_array)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], sorted_array)
        self.assertEqual(54, self.__measure.get_count())

    def testSortReverseOrdered(self):
        source_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted_array = self.__sort.sort(source_array)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], sorted_array)
        self.assertEqual(54, self.__measure.get_count())
