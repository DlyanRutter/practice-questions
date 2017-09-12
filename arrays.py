def binary_search(key, array):
    """
    implements binary search algorithm. returns the key of a given value if it
    is in an array. if the key is not in the array, returns None
    """
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + (high - low)/2

        if array[mid] == key:
            return mid

        if key < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
            
    return False
