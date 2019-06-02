# You are given a list of data entries that represent entries and
# exits of groups of people into a building. An entry looks like this:
#
# {"timestamp": 1526579928, count: 3, "type": "enter"}
#
# This means 3 people entered the building. An exit looks like this:
#
# {"timestamp": 1526580382, count: 2, "type": "exit"}
#
# This means that 2 people exited the building. timestamp is in Unix time.
#
# Find the busiest period in the building, that is, the time with the most
# people in the building. Return it as a pair of (start, end) timestamps.
# You can assume the building always starts off and ends up empty, i.e. with 0 people inside.

def solutin(events):
    people_counter = 0
    time_per_people = []
    for event in events:
        if event['type'] == 'enter':
            people_counter += event['count']
        else:
            people_counter -= event['count']

        time_per_people.append([event['timestamp'], people_counter])

    time_per_people.sort(key=lambda x: x[1], reverse=True)
    start = time_per_people[0][0]
    time_per_people.pop(0)
    time_per_people.pop(len(time_per_people) - 1)
    end = time_per_people[len(time_per_people) - 1][0]

    return (start, end)
