# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
# find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

def minClassrom(time):
    eventList = []

    for (start, end) in time:
        eventList.append((start, 'start'))
        eventList.append((end, 'end'))

    eventList.sort()

    required = 0
    toReteurn = 0

    for (time, event) in eventList:
        if event == 'start':
            required += 1
        elif event == 'end':
            required -=1 
        if required > toReteurn:
            toReteurn = required
    return toReteurn

print(minClassrom([(30, 75), (0, 50), (60, 150)]))