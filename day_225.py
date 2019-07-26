# There are N prisoners standing in a circle, waiting to be executed.
# The executions are carried out starting with the kth person,
# and removing every successive kth person going clockwise until there is no one left.

def solution(n, k):
    last = None
    next = 0

    prisoners = list(range(1, n + 1))

    while prisoners:
        next = (next + k - 1) % len(prisoners)
        last = prisoners[next]
        prisoners = prisoners[:next] + prisoners[next+1:]

    return last