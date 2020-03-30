# Best time to buy and sell stock III hard.

# time limit error (199/200 passed)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = len(prices)
        p = 0
        for i in range(0, m+1):
            tmp = self.profit(prices[:i]) + self.profit(prices[i:])
            p = max(p, tmp)
        return p
        
    def profit(self, prices):
        m = len(prices)
        if m <= 1:
            return 0
        l = prices[0] # lowest price
        p = 0  # max profit
        for i in range(1, m):
            v = prices[i]
            if v < l:
                l = v
            p = max(p, v-l)
        return p
            
# 5% solution (reduce the size of the outer loop)....
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = len(prices)
        p = 0
        
        cs = [0, m]
        for i in range(m):
            if (i-1 < 0  or prices[i] > prices[i-1]) and \
               (i+1 == m or prices[i] >= prices[i+1]):
                cs.append(i)
            
        
        for i in cs:
            tmp = self.profit(prices[:i+1]) + self.profit(prices[i+1:])
            p = max(p, tmp)
        return p
        
    def profit(self, prices):
        m = len(prices)
        if m <= 1:
            return 0
        l = prices[0] # lowest price
        p = 0  # max profit
        for i in range(1, m):
            v = prices[i]
            if v < l:
                l = v
            p = max(p, v-l)
        return p

# 60% solution
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = len(prices)
        if m <= 1:
            return 0

        lb = prices[0]
        p1 = [0] * m
        
        # left to right.
        for i in range(1, m):
            v = prices[i]
            if v < lb:
                lb = v
            p1[i] = max(p1[i-1], v-lb)
        
        p1.insert(0,0)
        
        # right to left
        ub = prices[-1]
        p2 = [0] * m
        for i in range(m-2, -1, -1):
            v = prices[i]
            if v > ub:
                ub = v
            p2[i] = max(p2[i+1], ub-v)
        p2.append(0)
        
        tot = 0
        for i in range(m+1):
            tot = max(tot, p1[i]+ p2[i])
            
        return tot

        
