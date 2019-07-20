# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def aum_up_to(table, k):
    table.sort()
	
    begin = 0
    end = len(table) - 1
	
    while begin < end:
        tmp_sum = table[begin] + table[end]
        if tmp_sum == k:
            return True
        elif tmp_sum > k:
            end = end - 1
        elif tmp_sum < k:
            begin = begin + 1
    return False

table = [10, 15, 3, 7]
aum_up_to(table, 17)
