# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

def longestConsecutive(array):
    array.sort()

    stop = 1

    for i in range(0, len(array) - 1):
        if array[i+1] - array[i] == 1:
            stop += 1
        else:
            break

    return array[0:stop]