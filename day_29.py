# Run-length encoding is a fast and simple method of encoding strings. 
# The basic idea is to represent repeated successive characters as a 
# single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

def code(string, before, cnt ,result):
    if len(string) == 0:
        return result
    elif string == before*len(string):
        return result + str(len(string)+1) + before
    elif before == string[0]:
        cnt += 1
        return code(string[1:], before, cnt, result)
    else:
        return code(string, string[0], 0, result  + str(cnt) + before)

def encode(string):
    return code(string, string[0], 0, '')

print(encode('AAAABBBCCDA'))
assert encode('AAAABBBCCDA') == '4A3B2C1D2A'