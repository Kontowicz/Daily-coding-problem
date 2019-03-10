# Implement division of two positive integers without using the division, 
# multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.

def div(a, b):
    c = a + b
    value = 0
    while c > b:
        c -= b
        value += 1
    return value

assert div(15, 3) == 5
assert div(20, 2) == 10
print('Test pass')