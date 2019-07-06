# Given i1, j1, i2, and j2, compute the number
# of elements of M smaller than M[i1, j1] 
# and larger than M[i2, j2].

def solution(matrix, i_1, i_2, j_1, j_2):
	num_1 = max(matrix[i_1][i_2], matrix[j_1][j_2])
	num_2 = min(matrix[i_1][i_2], matrix[j_1][j_2])
	
	print('num_1: {} num_2: {}'.format(num_1, num_2))
	
	counter = 0
	
	for row in matrix:
		counter += len([x for x in row if (x < num_1 and x > num_2)])
	print(counter)
	return counter
	
matrix = [[1, 3, 7, 10, 15, 20],
		[2, 6, 9, 14, 22, 25],
		[3, 8, 10, 15, 25, 30],
		[10, 11, 12, 23, 30, 35],
		[20, 25, 30, 35, 40, 45]]
		
assert solution(matrix, 1, 1, 3, 3) == 14

print('Test pass.')