# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

def clockwise(row, column, array):
    k = 0; l = 0      
  
    while (k < row and l < column) : 
        for i in range(l, column) : 
            print(array[k][i])               
        k += 1

        for i in range(k, row) : 
            print(array[i][column - 1]) 
        column -= 1

        if ( k < row) : 
              
            for i in range(column - 1, (l - 1), -1) : 
                print(array[row - 1][i]) 
            row -= 1

        if (l < column) : 
            for i in range(row - 1, k - 1, -1) : 
                print(array[i][l]) 
            l += 1

array = [[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

row = 4
colum = 5       

clockwise(row, colum, array)