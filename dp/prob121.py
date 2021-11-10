# 121 Best time to buy and sell stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        if n <= 1:
            return 0

        dp_l = [0] * n  # history of lowest prices before the day i
        dp_l[1] = prices[0]
        profits = [0] * n
        for i in range(2, n):
            dp_l[i] = min(prices[i-1], dp_l[i-1])

        for i in range(1, n):
            profits[i] = prices[i] - dp_l[i] if prices[i] > dp_l[i] else 0


        return max(profits)
