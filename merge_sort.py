class MergeSort:

    def __init__(self, operation_measure):
        self.__operation_measure = operation_measure

    def sort(self, arr):
        arr_len = len(arr)
        if arr_len <= 1:
            return arr
        else:
            mid = arr_len // 2
            left = self.sort(arr[0:mid])
            right = self.sort(arr[mid:])
            return self.__merge(left, right)

    def __get_item(self, arr, index):
        self.__operation_measure.increment()
        return arr[index]

    def __merge(self, left, right):
        merged = []
        right_index = 0
        right_len = len(right)
        right_value = self.__get_item(right, right_index)
        for left_index in range(0, len(left)):
            left_value = self.__get_item(left, left_index)
            while right_value and left_value > right_value:
                merged.append(right_value)
                right_index += 1
                if right_index < right_len:
                    right_value = self.__get_item(right, right_index)
                else:
                    right_value = None
            merged.append(left_value)
        for index in range(right_index, right_len):
            merged.append(self.__get_item(right, index))
        return merged
