import unittest

from measure import *
from quick_sort import *


class QuickSortTest(unittest.TestCase):

    __measure = CountMeasure()
    __sort = QuickSort(__measure)

    def testSort(self):
        source_array = [10, 4, 7, 4, 5]
        sorted_array = self.__sort.sort(source_array)
        self.assertEqual([4, 4, 5, 7, 10], sorted_array)
        self.assertEqual(11, self.__measure.get_count())
