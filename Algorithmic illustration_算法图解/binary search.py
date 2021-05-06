import math

def binary_search(list, item):
    """binary search
        list: An ordered array
        item: An element
        :return index
    """
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = math.floor((low + high) / 2)
        guess = list[mid]
        if item == guess:
            return mid
        if item > guess:
            low = mid + 1
        else:
            high = mid - 1
    return None



list = [1, 2, 3, 4, 5, 6]

print(binary_search(list, -1))