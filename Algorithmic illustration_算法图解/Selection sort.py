
# mine
def my_findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index, smallest

def my_selectionSort(arr):
    newArr = []
    while arr:
        smallest_index, smallest = my_findSmallest(arr)
        newArr.append(smallest)
        del arr[smallest_index]

    return newArr


# writer
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))

# print(findSmallest([5, 3, 6, 2, 10]))