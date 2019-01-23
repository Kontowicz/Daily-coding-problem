# Given an array of strictly the characters 'R', 'G', and 'B',
# segregate the values of the array so that all the Rs come first,
# the Gs come second, and the Bs come last. You can only swap elements of the array.
# Do this in linear time and in-place.
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
# it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

def sortRGB(array):
    left = 0
    rigth = len(array) - 1
    while left<rigth:
        while array[left] == 'R' and left < rigth:
            left += 1
        
        while array[rigth] != 'R' and left < rigth:
            rigth -= 1

        array[left], array[rigth] = array[rigth], array[left]
    
    rigth = len(array) - 1

    while left < rigth:
        while array[left] != 'B' and left < rigth:
            left += 1
        
        while array[rigth] == 'B' and left < rigth:
            rigth -= 1

        array[left], array[rigth] = array[rigth], array[left]
        
    return array
        
print(['G', 'B', 'R', 'R', 'B', 'R', 'G'])
print(sortRGB(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
assert sortRGB(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']