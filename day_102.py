# Given a list of integers and a number K, return which contiguous elements of the list sum to K.
def solution(array, k):
    currSum = array[0]
    start = 0
    i = 1
    while i <= len(array):
        while currSum > k and start < i - 1:
            currSum = currSum - array[start]

        if currSum == k:
            return array[start:i-1]

        if i < len(array):
            currSum = currSum + array[i]
        i += 1

    return None

print(solution([1, 2, 3, 4, 5], 9))