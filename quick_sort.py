from math import *

from array_generator import *
from measure import *


def sort(arr):
    arr_len = len(arr)
    if arr_len <= 1:
        return arr
    else:
        base = get_base(arr)
        arr_left = []  # [i for i in arr[1:] if i <= base]
        arr_right = []  # [i for i in arr[1:] if i > base]
        for item in arr[1:]:
            if item <= base:
                append_to_tail(arr_left, item)
            elif item > base:
                append_to_tail(arr_right, item)
        return sort(arr_left) + [base] + sort(arr_right)


def get_item(arr, index):
    operation_measure.increment()
    return arr[index]


def append_to_tail(arr, item):
    operation_measure.increment()
    arr.append(item)


def get_base(arr):
    return get_item(arr, 0)


operation_measure = CountMeasure()
requested_length = int(input("Print array length:"))
source = generate_array(requested_length)
print("Source array: {}".format(source))
ordered = sort(source)
print("Ordered array ({} items): {}".format(len(ordered), ordered))
print("Access count: {}".format(operation_measure.get_count()))
source_length = len(source)
n_x_log_n = source_length * log2(source_length)
print("O(n*log(n)): {}".format(n_x_log_n))
print("O(n*n): {}".format(source_length * source_length))
