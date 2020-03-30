# 122 Best Time to Buy and Sell Stock II

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = len(prices)
        if m <= 1:
            return 0
        
        lp  = prices[0] # lowest prices so far
        pc  = 0         # profit of current round
        tot = 0         # total profit
        for i in range(1, m):
            p = prices[i] # current price
            if p > prices[i-1]:
                pc = max(pc, p - lp)
            elif p < prices[i-1]:
                lp = p
                tot += pc
                pc = 0
        tot += pc
        return tot

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = len(prices)
        if m <= 1:
            return 0
        
        p = 0
        for i in range(1, m):
            if prices[i] > prices[i-1]:
                p += prices[i] - prices[i-1]
            
        return p
        

