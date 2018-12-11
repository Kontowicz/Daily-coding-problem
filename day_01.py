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