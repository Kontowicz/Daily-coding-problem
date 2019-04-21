# Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2].
def rotate(array, k):
    k = k % len(array)
    tmp = array*2
    return tmp[k:k+len(array)]

