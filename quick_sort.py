import math
import random

access_count = 0


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
    increment_access_counter()
    return arr[index]


def append_to_tail(arr, item):
    increment_access_counter()
    arr.append(item)


def increment_access_counter():
    global access_count
    access_count += 1


def get_base(arr):
    return get_item(arr, 0)


def generate_array(length):
    arr = []
    for q in range(0, length):
        arr.append(random.randrange(1, length * 2))
    return arr


requested_length = int(input("Print array length:"))
source = generate_array(requested_length)
print("Source array: {}".format(source))
ordered = sort(source)
print("Ordered array ({} items): {}".format(len(ordered), ordered))
print("Access count: {}".format(access_count))
source_length = len(source)
n_x_log_n = source_length * math.log2(source_length)
print("O(n*log(n)): {}".format(n_x_log_n))
print("O(n*n): {}".format(source_length * source_length))
