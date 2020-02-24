from math import log2

from algorithms.sort import *


class TimSort(Sort):

    def sort(self, arr):
        array_length = len(arr)
        min_run = self.__min_run(arr)
        print(min_run)
        runs = []
        run = []
        asc = None
        last = None
        index = 0
        while index < array_length:
            item = self._get_item(arr, index)
            if run:
                length = len(run)
                greater = item >= last
                if asc is None:
                    asc = greater
                if asc != greater:
                    if length >= min_run:
                        self.__add_run(run, runs, asc)
                        run = []
                        asc = None
                        last = None
                        continue
                    else:
                        self.__insert(item, run, asc)
                        index += 1
                        continue
            run.append(item)
            index += 1
            last = item
        if run:
            self.__add_run(run, runs, asc)
        print(runs)
        return self.__merge(runs)

    def complexity(self, n):
        return "O(n * log(n)): " + str(int(n * log2(n)))

    def __insert(self, item, run, asc):
        for q in range(0, len(run)):
            if asc:
                if item <= self._get_item(run, q):
                    run.insert(q, item)
                    break
            else:
                if item >= self._get_item(run, q):
                    run.insert(q, item)
                    break

    def __add_run(self, run, runs, asc):
        runs.append(run if asc else self.__reverse(run))

    def __reverse(self, array):
        reversed_array = []
        for index in reversed(range(0, len(array))):
            reversed_array.append(self._get_item(array, index))
        return reversed_array

    def __merge(self, runs):
        count = len(runs)
        if count == 1:
            return runs[0]
        else:
            mid = count // 2
            left = self.__merge(runs[:mid])
            right = self.__merge(runs[mid:])
            left_length = len(left)
            right_length = len(right)
            left_index = 0
            right_index = 0
            merged = []
            left_value = None
            right_value = None
            while left_index < left_length and right_index < right_length:
                if not left_value:
                    left_value = self._get_item(left, left_index)
                if not right_value:
                    right_value = self._get_item(right, right_index)
                if left_value <= right_value:
                    merged.append(left_value)
                    left_index += 1
                    left_value = None
                else:
                    merged.append(right_value)
                    right_index += 1
                    right_value = None
            if left_index < left_length:
                merged += left[left_index:]
            elif right_index < right_length:
                merged += right[right_index:]
            return merged

    @staticmethod
    def __min_run(arr):
        n = len(arr)
        remainder = 0
        while n >= 64:
            remainder += n % 2
            n //= 2
        return n + remainder
