# An sorted array of integers was rotated an 
# unknown number of times. Given such an array, 
# find the index of the element in the array in 
# faster than linear time. If the element 
# doesn't exist in the array, return null.

def solution(array, begin, end, value):
	if begin == end:
		return
		
	pivot = begin + ((end - begin) // 2)
	
	if array[pivot] == value:
		return pivot
	elif array[pivot] > value:
		if array[begin] >= value:
			return solution(array, begin, pivot, value)
		else:
			return solution(array, pivot, end, value)
	elif array[pivot] < value:
		if array[begin] <= value:
			return solution(array, begin, pivot, value)
		else:
			return solution(array, pivot, end, value)
			
def run(array, value):
	return solution(array, 0, len(array), value)
