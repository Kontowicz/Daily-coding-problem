# Given a array of numbers representing the stock prices of a company in chronological order,
# write a function that calculates the maximum profit you could have made from buying and 
# selling that stock once. You must buy before you can sell it.

def maximumProfit(arr):
    profit = -1
    buy_price = 0
    sell_price = 0
    index = True
    
    for i in range(0, len(arr)-1):
        sell_price = arr[i+1]

        if index: 
            buy_price = arr[i]

        if sell_price < buy_price:
            index = True 
            continue
        else:
            prof = sell_price - buy_price
            if prof > profit:
               profit = prof
            index = False
        
    return profit

print(maximumProfit([9, 11, 8, 5, 7, 10]))

assert maximumProfit([9, 11, 8, 5, 7, 10]) == 5