import numpy as np

class Arrays(object):
    def __init__(self, array):
        self.array = array

    def binary_search(self, key):
        """
        given a sorted array of integers return the index of the given key
        runtime = O(logn), memory complexity = O(1). At every step, consider
        the array between low and high indices. Calculate the mid index
        if mid index is key, return mid. If element at mid is > key, reduce
        the array size such that high becomes mid - 1. If element at mid is <
        key, reduce array size such that low becomes mid + 1. When low > high,
        doesn't exist. Return -1
        """
        low_index = 0
        high_index = len(self.array) - 1

        while low_index <= high_index:

            #python rounds down
            mid_index = low_index + ((high_index - low_index) / 2)

            if self.array[mid_index] == key:
                return mid_index
            
            if key < self.array[mid_index]:
                high_index = mid_index - 1
            else:
                low_index = mid_index + 1

        return -1

array = [1, 10, 20, 47, 59, 63, 77, 88, 99, 111]
key = 77


def binary(array, key):
    low = 0
    high = len(array) - 1

    while low<=high:
        mid = low + (high - low) / 2

        if array[mid] == key:
            return mid

        if key < array[mid]:
            high = mid - 1

        else:
            low = mid + 1
    return -1

print binary(array, key)










