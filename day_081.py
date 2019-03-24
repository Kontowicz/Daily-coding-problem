# Given a mapping of digits to letters (as in a phone number), and a digit string,
# return all possible letters the number could represent. You can assume each 
# valid number in the mapping is a single digit.

def mapping(array, number):
    out = ['']
    pres = []
    for num in number:
        letters = array[num]
        if len(letters) == 0:
            continue
        for item in out:
            for i in letters:
                pres.append(item + i)
        out = pres
        pres = []

    return out

print(mapping({'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i']}, '234'))