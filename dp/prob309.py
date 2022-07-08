# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/2200780/Simple-DP-State-machine-DP

# weird cycles
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        hold = [0] * n
        cool = [0] * n
        unhold = [0] * n

        hold[0] = -prices[0]

        for i in range(1, n):
            hold[i] = max(hold[i-1],  cool[i-1]-prices[i])
            unhold[i] = max(unhold[i-1], hold[i-1] + prices[i])
            cool[i] = max(cool[i-1], unhold[i-1])
        return max(unhold[n-1], cool[n-1])
