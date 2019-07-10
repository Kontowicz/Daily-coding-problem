# Given an undirected graph represented as an adjacency 
# matrix and an integer k, write a function to determine 
# whether each vertex in the graph can be colored such 
# that no two adjacent vertices share the same color 
# using at most k colors.

def solution(matrix, k):
	for row in matrix:
		if len([x for x in row if x == 1]) >= k:
			return False
	
	return True