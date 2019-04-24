# Given a real number n, find the square root of n. For example, given n = 9, return 3.

def solution(value):
    if value == 0 or value == 1:
        return value

    start = 1
    end = value

    while start <= end:
        mid = (start + end) // 2
        midPow = mid * mid

        if midPow == value:
            return mid

        if midPow < value:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

    return ans

print(solution(9))