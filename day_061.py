# Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

def power(x, y):
    result = x
    for _ in range(1, y):
        result *= x
    return result

print(power(2,3))
print(power(2,10))
print(power(3,3))