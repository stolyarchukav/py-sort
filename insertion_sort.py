from sort import *


class InsertionSort(Sort):

    def sort(self, arr):
        length = len(arr)
        for index in range(0, length):
            for index_2 in range(0, index):
                item = self._get_item(arr, index)
                item_2 = self._get_item(arr, index_2)
                if item < item_2:
                    arr[index] = item_2
                    arr[index_2] = item
        return arr

