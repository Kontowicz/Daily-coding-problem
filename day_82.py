# Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

file = 'Hello world'
def read7():
    global file
    data = file[0:7]
    file = file[7:]
    return data

def readN(number):
    cnt = number
    array = []
    while number > 0:
        array.append(read7())
        number -= 7
    
    return ''.join(array)[0:cnt]

print(readN(2))
