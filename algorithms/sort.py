class Sort:

    def __init__(self, operation_measure):
        """Constructor"""
        self.__operation_measure = operation_measure

    def sort(self, arr):
        """Return sorted array"""
        pass

    def _get_item(self, arr, index):
        """Return an item retrieved by an index from array. Includes measuring (increment access counter)"""
        self.__operation_measure.increment()
        return arr[index]

    def complexity(self, n):
        """Return expected complexity in O notation"""
        pass
