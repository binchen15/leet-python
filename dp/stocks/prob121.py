# 121 Best Time to Buy and Sell Stock

# O(n) space complexity
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = len(prices)
        if m <= 1:
            return 0
        lp      = [0] * m   # lowest prices up to day[i]
        profits = [0] * m   # maximum profits up to day[i]
        lp[0]   = prices[0]
        profits[0] = 0
        for i in range(1, m):
            lp[i] = min(lp[i-1], prices[i]) 
            profits[i] = max(profits[i-1], prices[i] - lp[i])
        return profits[m-1]        


#O(1) space complexity
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = len(prices)
        if m <= 1:
            return 0
        lp      = prices[0] # lowest prices up to day[i]
        profits = 0   # maximum profits up to day[i]
        for i in range(1, m):
            lp = min(lp, prices[i])
            if prices[i] > lp:
                profits = max(profits, prices[i] - lp)
        return profits        
