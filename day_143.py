# Given a pivot x, and a list lst, partition the list into three parts.

#     The first part contains all elements in lst that are less than x
#     The second part contains all elements in lst that are equal to x
#     The third part contains all elements in lst that are larger than x

# Ordering within a part can be arbitrary.

# For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].

def solution(array, pivot):
    first = []
    second = []
    third = []

    for item in array:
        if item < pivot:
            first.append(item)
        if item == pivot:
            second.append(item)
        if item > pivot:
            third.append(item)

    return first + second + third

assert solution([9, 12, 3, 5, 14, 10, 10], 10) ==  [9, 3, 5, 10, 10, 12, 14]