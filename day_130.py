# Given an array of numbers representing the stock arrays of a company 
# in chronological order and an integer k, return the maximum profit
# you can make from k buys and sells. You must buy the stock before you 
# can sell it, and you must sell the stock before you can buy it again.

def solution(array, k):
    profit = [[0 for i in range(len(array) + 1)]  
                 for j in range(k + 1)]  

    for i in range(1, k + 1):  
        value = float('-inf') 
          
        for j in range(1, len(array)):  
            value = max(value, 
                           profit[i - 1][j - 1] - 
                           array[j - 1])  
            profit[i][j] = max(profit[i][j - 1],  
                               array[j] + value)  
  
    return profit[k][len(array) - 1]  

print(solution([5, 2, 4, 0, 1], 2))