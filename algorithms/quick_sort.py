from math import log2

from algorithms.sort import *


class QuickSort(Sort):

    def sort(self, arr):
        arr_len = len(arr)
        if arr_len <= 1:
            return arr
        else:
            base = self.__get_base(arr)
            arr_left = []  # [i for i in arr[1:] if i <= base]
            arr_right = []  # [i for i in arr[1:] if i > base]
            for index in range(1, arr_len):
                item = self._get_item(arr, index)
                if item <= base:
                    arr_left.append(item)
                elif item > base:
                    arr_right.append(item)
            return self.sort(arr_left) + [base] + self.sort(arr_right)

    def __get_base(self, arr):
        return self._get_item(arr, 0)

    def complexity(self, n):
        return "O(n * log(n)): " + str(n * log2(n))
