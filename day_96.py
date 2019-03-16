# Given a number in the form of a list of digits, return all possible permutations.

def getPerm(array, size):
    a = []
    def permutation(array, size):
        if size == 1:
            a.append(array)
            return array

        for i in range(0, size):
            permutation(array, size - 1)

            if size % 2 == 1:
                array[0], array[size - 1] = array[size - 1], array[0]
            else:
                array[i], array[size - 1] = array[size - 1], array[i]

    permutation(array, size)
    return a

print(getPerm([1,2,3], 3))