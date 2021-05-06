

# recursion
def DaC_sum(list):
    """sum of the elements of a list"""
    if list == []:
        return 0
    else:
        x = list[0]
        return x + DaC_sum(list[1:])


def DaC_len(list):
    """number of the elements of a list"""
    if list == []:
        return 0
    else:
        return 1 + DaC_len(list[1:])


def DaC_biggest(list):
    """find the biggest element of a list"""
    if list == []:
        return 0
    else:
        x = list[0]
        return max(x, DaC_biggest(list[1:]))


mylist = [2, 18, 5, 6]
# print(DaC_sum(mylist))
# print(DaC_len(mylist))
print(DaC_biggest(mylist))
