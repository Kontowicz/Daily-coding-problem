# A number is considered perfect if its digits sum up to exactly 10.
# Given a positive integer n, return the n-th perfect number.

def sum(number):
    toReturn = 0
    while number != 0:
        toReturn += number % 10
        number = int(number / 10)
    return toReturn

def getNumber(n):
    start = 0
    cnt = 0
    while True:
        s = sum(start)
        if s == 10:
            cnt+=1
        
        if cnt == n:
            return start
        start += 1
        
    
print(getNumber(1))
print(getNumber(2))
