# Given a collection of intervals, find the minimum number of
# intervals you need to remove to make the rest of the intervals non-overlapping.
def solution(array):
    intervals = sorted(array, key = lambda x:x[1])
    counter = 0

    time = intervals[0][1]
    for iter in intervals:

        if iter[0] >= time:
            counter += 1
        time = iter[1]

    return counter


