# Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).

import random 

def solution(n, l):
    rand = random.randint(0, n - 1)

    if rand in l:
        return solution(n, l)

    return rand
