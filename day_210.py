# A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:
#     if n is even, the next number in the sequence is n / 2
#     if n is odd, the next number in the sequence is 3n + 1


def solution(number, sequence = []):
    if number == 1:
        return sequence
    if number % 2 == 0:
        solution(number // 2, sequence.append(number))
    else:
        solution(3*number+1, sequence.append(number))