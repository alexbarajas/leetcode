from typing import List


def maxProfit(prices: List[int]) -> int:
    # 0. if the prices list has less than 2 values, return 0
    if len(prices) < 2:
        return 0

    # 1. set the buy variable as infinity, and the profit variable as 0
    buy = float("inf")
    profit = 0

    # 2. go thru each price in prices, buy the min between the outstanding buy and the current price, and profit is the max between the outstanding profit, and the current price minus the outstanding buy
    for price in prices:
        buy = min(buy, price)
        profit = max(profit, price - buy)

    # 3. return the max profit
    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]) == 5)
print(maxProfit([7, 6, 4, 3, 1]) == 0)
