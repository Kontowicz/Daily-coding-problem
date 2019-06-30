# Given a set of distinct positive integers, find the largest subset
# such that every pair of elements in the subset (i, j)
# satisfies either i % j = 0 or j % i = 0.

def solution(array):
    results = []
    array.sort(reverse = True)

    for i in range(0, len(array)):
        tmp = [array[i]]
        for j in range(i + 1, len(array)):
            if array[i] % array[j] == 0 or array[j] % array[i] == 0:
                tmp.append(array[j])
        results.append(tmp)

    return max(results, key = len)