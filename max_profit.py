# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    best_profit = 0
    current_profit = 0
    previous_price = None
    for price in A:
        #if (current_profit + (price - previous_price)) < 0 then there's no profit when selling today.
        #the price is too low.
        #Therefore, we should reset the start date to buy.
        if None != previous_price:
            current_profit = max(0,current_profit + (price - previous_price))
            best_profit = max(best_profit, current_profit)
        previous_price = price
    
    return best_profit

A = [5, 8, 2, 15]
print(solution(A))