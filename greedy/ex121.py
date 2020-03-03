class Solution(object):
    """time exceeded error"""	
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p = 0   # max profit
        m = len(prices)
        for j in range(1, m): # day of selling
            for i in range(j):  # day of buying
                p0 = prices[j] - prices[i] 
                if p0 > p:
                    p = p0
        return p

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = len(prices)
        if m <= 1:
            return 0
        buy    = prices[0]
        profit = 0
        for i in range(1, m):
            if prices[i] < buy: # reget buying price
                buy = prices[i]
                # do not update profit, not sell today
            elif prices[i] - buy > profit: # reconsider sell
                profit =prices[i] - buy 
        return profit


