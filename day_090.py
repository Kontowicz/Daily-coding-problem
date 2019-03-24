# Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).

import random 

def solution(n, l):
    rand = random.randint(0, n - 1)

    if rand in l:
        return solution(n, l)

    return rand

def solution_01(n, l):
    list = []
    for i in range(0, n):
        if i not in l:
            list.append(i)

    return list[random.randint(0, len(list) - 1)]


print(solution_01(10, [1,2,4,5]))