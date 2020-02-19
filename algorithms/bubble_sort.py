from algorithms.sort import *


class BubbleSort(Sort):

    def sort(self, arr):
        array_length = len(arr)
        changed = True
        while changed:
            changed = False
            previous_index = 0
            first = self._get_item(arr, previous_index)
            for index in range(1, array_length):
                second = self._get_item(arr, index)
                if first > second:
                    arr[previous_index] = second
                    arr[index] = first
                    changed = True
                else:
                    first = second
                previous_index = index
        return arr

    def complexity(self, n):
        return "O(n * n): " + str(n * n)
