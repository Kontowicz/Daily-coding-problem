# We can determine how "out of order" an array A is by counting the number of inversions it has.
# Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

def countInversion(array):
    count = 0
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                count += 1
    return count

print(countInversion( [2, 4, 1, 3, 5]))