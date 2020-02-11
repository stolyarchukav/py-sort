from sort import *


class InsertionSort(Sort):

    def __init__(self, operation_measure):
        self.__operation_measure = operation_measure

    def sort(self, arr):
        length = len(arr)
        for index in range(0, length):
            for index_2 in range(0, index):
                item = self.__get_item(arr, index)
                item_2 = self.__get_item(arr, index_2)
                if item < item_2:
                    arr[index] = item_2
                    arr[index_2] = item
        return arr

    def __get_item(self, arr, index):
        self.__operation_measure.increment()
        return arr[index]
