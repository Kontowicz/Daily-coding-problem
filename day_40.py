# Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.
def solution(array):
    first = 0
    second = 0
    for element in array:
        second = second | (first & element)

        first = first ^ element

        bm = ~(first & second)

        first &=  bm 
        second &= bm
    return first

print('[6, 1, 3, 3, 3, 6, 6]')
print(solution([6, 1, 3, 3, 3, 6, 6]))
assert solution([6, 1, 3, 3, 3, 6, 6]) == 1

print('[13, 19, 13, 13]')
print(solution([13, 19, 13, 13]))
assert solution([13, 19, 13, 13]) == 19