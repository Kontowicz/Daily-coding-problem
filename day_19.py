# A builder is looking to build a row of N houses that can be of K different colors.
# He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
# return the minimum cost which achieves this goal.

def minimumCost(matrix):
    cost = [0] * len(matrix[0])

    for row in matrix:
        tmp = [0] * len(matrix[0])
        for i in range(0, len(row)):
            tmp[i] = row[i] + min(cost[:i] + cost[i + 1:])
        
        cost = tmp

    return min(cost)

print(minimumCost([
                [2, 1, 1],
                [1, 10, 3],
                [1, 2, 100]
                ]))