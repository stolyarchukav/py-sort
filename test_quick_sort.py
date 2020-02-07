from math import log2
from array_generator import *
from measure import *
from quick_sort import *


operation_measure = CountMeasure()
sorter = QuickSort(operation_measure)
requested_length = int(input("Print array length:"))
source = generate_array(requested_length)
print("Source array: {}".format(source))
ordered = sorter.sort(source)
print("Ordered array ({} items): {}".format(len(ordered), ordered))
print("Access count: {}".format(operation_measure.get_count()))
source_length = len(source)
n_x_log_n = source_length * log2(source_length)
print("O(n*log(n)): {}".format(n_x_log_n))
print("O(n*n): {}".format(source_length * source_length))