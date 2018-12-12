#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

table = [10, 15, 3, 7]
k = 17

def sumUpTo(table, k):
    table.sort()
    begin = 0
    end = len(table) - 1
    while begin < end:
        s = table[begin] + table[end]
        if s == k:
            print('Yes')
            return
        elif s > k:
            end = end - 1
        elif s < k:
            begin = begin + 1
    print('No')

sumUpTo(table, 100)