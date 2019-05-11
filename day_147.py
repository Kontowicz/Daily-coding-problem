# Gray code is a binary code where each successive value differ 
# in only one bit, as well as when wrapping around. Gray code is 
# common in hardware so that we don't see temporary spurious values during transitions.

# Given a number of bits n, generate a possible gray code for it.

def solution(n):
    N = 1 << n
    result = []
    for i in range(0, N):

        x = i ^ (i >> 1)
        result.append(bin(x)[2:].zfill(n))
        
    return result