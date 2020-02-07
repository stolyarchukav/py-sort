class QuickSort:

    def __init__(self, operation_measure):
        self.__operation_measure = operation_measure

    def sort(self, arr):
        arr_len = len(arr)
        if arr_len <= 1:
            return arr
        else:
            base = self.__get_base(arr)
            arr_left = []  # [i for i in arr[1:] if i <= base]
            arr_right = []  # [i for i in arr[1:] if i > base]
            for item in arr[1:]:
                if item <= base:
                    self.__append_to_tail(arr_left, item)
                elif item > base:
                    self.__append_to_tail(arr_right, item)
            return self.sort(arr_left) + [base] + self.sort(arr_right)

    def __get_item(self, arr, index):
        self.__operation_measure.increment()
        return arr[index]

    def __append_to_tail(self, arr, item):
        self.__operation_measure.increment()
        arr.append(item)

    def __get_base(self, arr):
        return self.__get_item(arr, 0)

