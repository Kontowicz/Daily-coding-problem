# We say a number is sparse if there are no adjacent ones in its binary representation.
# For example, 21 (10101) is sparse, but 22 (10110) is not. For a given input N,
# find the smallest sparse number greater than or equal to N.



def solution(number):
    binary = str(bin(number)[2:])

    to_return = ''
    previous_digit = None
    flag = False
    for i, current_digit in enumerate(binary):
        if current_digit == '1' and previous_digit == '1':
            flag = True
        if flag:
            to_return += '0' * (len(binary) - i)
            break
        else:
            to_return += current_digit
        previous_digit = current_digit
    if flag:
        if to_return[0] == '1':
            to_return = '10' + to_return[1:]
        else:
            to_return = '1' + to_return

    return int(to_return, base=2)