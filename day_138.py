# Find the minimum number of coins required to make n cents.

# You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

# For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.


def findMaxMin(value, array):

    for item in array:
        if item <= value:
            return item

def solution(money, denom):
    denom = sorted(denom)[::-1]

    counter = 0

    while money != 0:
        money -= findMaxMin(money, denom)
        counter += 1

    return counter

denoms = [1, 5, 10, 25]

assert solution(16, denoms) == 3
assert solution(90, denoms) == 5
assert solution(100, denoms) == 4

print('Test pass.')