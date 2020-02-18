from datetime import *

from utils.array_generator import *
from algorithms.insertion_sort import *
from utils.measure import *

operation_measure = CountMeasure()
sorter = InsertionSort(operation_measure)
requested_length = int(input("Print array length:"))
source = generate_array(requested_length)
print("Source array: {}".format(source))
startTime = datetime.now().microsecond
ordered = sorter.sort(source)
endTime = datetime.now().microsecond
print("Ordered array ({} items): {}".format(len(ordered), ordered))
print("Time taken: {} microseconds".format(endTime - startTime))
print("Access count: {}".format(operation_measure.get_count()))
source_length = len(source)
print("O(n*n): {}".format(source_length * source_length))
