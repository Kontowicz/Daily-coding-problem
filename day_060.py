# Given a multiset of integers, return whether it
# can be partitioned into two subsets whose sums are the same.

def help(set, start, stop, sum, total):
    if start >= stop:
        return False
    if sum == total:
        return True

    return help(set, start + 1, stop, sum + set[start], total - set[start]) or help(set, start, stop - 1, sum + set[stop], total - set[stop])

def solution(set):
    if sum(set) % 2 == 1:
        return False

    set.sort()

    return help(set, 0, len(set) - 1, 0, sum(set))