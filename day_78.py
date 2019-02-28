# Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.

def merge(first, second):
    toreturn = []
    f = 0
    s = 0

    while f < len(first) and s < len(second):
      
        if first[f] < second[s]:
            toreturn.append(first[f])
            f += 1
        elif first[f] > second[s]:
            toreturn.append(second[s])
            s += 1
        else:
            toreturn.append(first[f])
            toreturn.append(second[s])
            f += 1
            s += 1

    toreturn += first[f:]
    toreturn += second[s:]
    return toreturn

def mergeAll(array):
    toReturn = array[0]

    for i in range(1, len(array)):
        toReturn = merge(toReturn, array[i])

    return toReturn
    

print(mergeAll([[1,3,5,7], [0,9,10,11], [2,4,6,8]]))
assert mergeAll([[1,3,5,7], [0,9,10,11], [2,4,6,8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
