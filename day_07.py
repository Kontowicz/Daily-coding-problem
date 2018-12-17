# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
# count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded 
# as 'aaa', 'ka', and 'ak'.

def count(message):
    cnt = [0]*(len(message) + 1)
    cnt[0] = 1
    cnt[1] = 1

    for i in range(2, len(message) + 1):
        if message[i - 1] > '0':
            cnt[i] = cnt[i-1]

        if message[i - 2] == '1' or (message[i - 2] == '2' and message[i - 1] < '7'):
            cnt[i] += cnt[i-2]
    return cnt[-1]

assert count("111") == 3