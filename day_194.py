# Suppose you are given two lists of n points, one list p1, p2, ..., pn
# on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1.
# Imagine a set of n line segments connecting each point pi to qi.
# Write an algorithm to determine how many pairs of the line segments intersect.

def solution(left, right):
    lines = list(zip(left, right))

    cnt = 0
    for i in range(len(lines)):
        for k in range(i):
            point_1, point_2 = lines[i], lines[k]
            if (point_1[0] < point_2[0] and point_1[1] > point_2[1]) or \
                    (point_1[0] > point_2[0] and point_1[1] < point_2[1]):
                cnt += 1

    return cnt