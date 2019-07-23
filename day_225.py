

def solution(n, k):
    last = None
    next = 0

    prisoners = list(range(1, n + 1))

    while prisoners:
        next = (next + k - 1) % len(prisoners)
        last = prisoners[next]
        prisoners = prisoners[:next] + prisoners[next+1:]

    return last

assert solution(5, 2) == 3
assert solution(3, 2) == 3
assert solution(5, 3) == 4