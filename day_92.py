# We're given a hashmap associating each courseId key with a list of courseIds values, 
# which represents that the prerequisites of courseId are courseIds. Return a sorted 
# ordering of courses such that we can finish all courses.
# Return null if there is no such ordering.


def prerequisite(hashmap):
    tmp = []
    for key, value in hashmap.items():
        if tmp == []:
            for v in value:
                tmp.append(v)
            tmp.append(key)
        else:
            pos = tmp.index(key)
            if pos == -1:
                return None
            for item in value:
                tmp.insert(pos, item)
                pos += 1
    
    toReturn = []

    for i in range(0, len(tmp)):
        if tmp[i] not in tmp[i+1:]:
            toReturn.append(tmp[i])

    return toReturn


print(prerequisite({'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}))
assert prerequisite({'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}) == ['CSC100', 'CSC200', 'CSC300']

print('Test pass')