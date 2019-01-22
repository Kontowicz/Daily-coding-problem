# Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, 
# and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. 
# If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.
# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] 
# and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].
# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.
# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', 
# you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.

def getPath(array, start):
    dictionay = {}
    for element in array:
        dictionay[element[0]] = element[-1]
    path = []
    if start not in dictionay:
        return None

    path.append(start)
    while start in dictionay:
        start = dictionay[start]
        path.append(start)

    return path

print([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] )
print(getPath([['SFO', 'HKO'], ['YYZ', 'SFO'], ['YUL', 'YYZ'], ['HKO', 'ORD']], 'YUL' ))
assert getPath([['SFO', 'HKO'], ['YYZ', 'SFO'], ['YUL', 'YYZ'], ['HKO', 'ORD']], 'YUL' ) == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
