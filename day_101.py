# Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

def aratosthenes(stop):
    isPrime = [0] * (stop + 1)
    for i in range(2, stop+1):
        isPrime[i] = True
    p = 2 
    while(p*p <= stop):
        if isPrime[p] == True:
            i = p * 2
            while i <= stop:
                isPrime[i] = False
                i += p
        p += 1
    
    return isPrime

def findPrimeSum(value):
    primeNum = aratosthenes(value)
    for i in range(0, value):
        if primeNum[i] and primeNum[value-i]:
            return i, value-i

print(findPrimeSum(4))