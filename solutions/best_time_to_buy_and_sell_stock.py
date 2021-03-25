import sys


def maxProfit(self, prices):
    min = sys.maxsize
    max_profit = 0

    for i in prices:
        if i < min:
            min = i
        elif i - min > max_profit:
            max_profit = i - min
    return max_profit
