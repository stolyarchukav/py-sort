from datetime import *

from algorithms.bubble_sort import *
from algorithms.insertion_sort import *
from algorithms.merge_sort import *
from algorithms.quick_sort import *
from algorithms.tim_sort import *
from utils.array_generator import *
from utils.measure import *

algorithms = {
        1: InsertionSort,
        2: MergeSort,
        3: QuickSort,
        4: BubbleSort,
        5: TimSort
    }


def get_algorithm():
    alg = algorithms.get(int(input("""Choose an algorithm: 
      \t1 - Insertion sort
      \t2 - Merge sort
      \t3 - Quick sort
      \t4 - Bubble sort
      \t5 - Tim sort
      :""")))
    if alg is None:
        raise Exception("Algorithm does not exist")
    return alg


algorithm = get_algorithm()
operation_measure = CountMeasure()
sorter = algorithm(operation_measure)

requested_length = int(input("Print array length:"))
source_array = generate_array(requested_length)

print("Source array: {}".format(source_array))

startTime = datetime.now().microsecond
sorted_array = sorter.sort(source_array)
endTime = datetime.now().microsecond

print("Sorted array ({} items): {}".format(len(sorted_array), sorted_array))
print("Time taken: {} microseconds".format(endTime - startTime))
print("Access count: {}".format(operation_measure.get_count()))
print("Expected complexity: {}".format(sorter.complexity(len(source_array))))
