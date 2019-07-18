# Convert Roman numer to decimal value.

values = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

def solution(string):
    if not string:
        return 0

    char = string[-1]
    val = values[char]
    for c in reversed(string[:-1]):
        val += values[c] * (-1 if values[c] < values[char] else 1)
        char = c
    return vals