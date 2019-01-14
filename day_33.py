# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.
# Recall that the median of an even-numbered list is the average of the two middle numbers.


def median(array):
    array.sort()
    if len(array) % 2 == 1:
        return array[int((len(array)-1)/2)] 
    else :
        return (array[int((len(array)-1)/2)]  + array[int((len(array)-1)/2+1)]) / 2

def runncingMedian(array):
    steram = []
    for element in array:
        steram.append(element)
        print(median(steram))

runncingMedian([2, 1, 5, 7, 2, 0, 5])