# A permutation can be specified by an array P, 
# where P[i] represents the location of the element at i in the permutation.

def solution(array, order):
	result = []
	for item in order:
		result.append(array[item])
		
	return result
	
	
assert solution(["a", "b", "c"], [2, 1, 0]) == ["c", "b", "a"]
