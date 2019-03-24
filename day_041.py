# Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, 
# and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. 
# If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.
# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] 
# and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].
# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.
# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', 
# you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.

def getPath(array, start):
    array.sort(key=lambda x:x[-1])


    dictionay = {}
    dictionay_second = {}
    for element in array:
        if element[0] not in dictionay:
            dictionay[element[0]] = element[-1]
        else:
            dictionay_second[element[0]] = element[-1]

    path = []
    if start not in dictionay:
        return None
    before = start
    path.append(start)

    while start in dictionay:
        before = start
        start = dictionay[start]
        if before in  dictionay_second:
            dictionay[before] = dictionay_second[before]
            del dictionay_second[before]
            path.append(start)
            continue

        del dictionay[before]

        path.append(start)
    if len(dictionay) > 0:
        return None
    return path

print([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] )
print(getPath([['SFO', 'HKO'], ['YYZ', 'SFO'], ['YUL', 'YYZ'], ['HKO', 'ORD']], 'YUL' ))
assert getPath([['SFO', 'HKO'], ['YYZ', 'SFO'], ['YUL', 'YYZ'], ['HKO', 'ORD']], 'YUL' ) == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

print([['SFO', 'COM'], ['COM', 'YYZ']])
print(getPath([['SFO', 'COM'], ['COM', 'YYZ']], 'COM'))
assert getPath([['SFO', 'COM'], ['COM', 'YYZ']], 'COM') == None

print([['SFO', 'COM'], ['COM', 'YYZ']])
print(getPath([['A', 'B'], ['A', 'C'], ['B', 'C'], ['C', 'A']], 'A'))
assert getPath([['A', 'B'], ['A', 'C'], ['B', 'C'], ['C', 'A']], 'A') == ['A', 'B', 'C', 'A', 'C']