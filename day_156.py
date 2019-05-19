
def solution(number):
    array = [0, 1, 2, 3]

    for i in range(4, number + 1):
        array.append(i)
        for x in range(1, i+1):
            tmp = x * x
            if tmp > i:
                break
            else:
                array[i] = min(array[i], 1 + array[i - tmp])

    return array[number]

print(solution(4))