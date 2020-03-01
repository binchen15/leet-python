class Solution(object):
    """multile round stock transaction"""
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = len(prices)
        if m <= 1:
            return 0
        buy  = prices[0] # current best buy
        make = 0         # current profit
        tot  = 0         # total profile multi-rounds
        prev = prices[0] # price at previous day
        for i in range(1, m):
            curr = prices[i]
            if curr >= prev:
                temp = curr - buy
                if temp > make:
                    make = temp
            else: # price goes down
                if make > 0:  # close the previous round
                    tot += make
                buy  = curr   # new round
                make = 0
            prev = curr
        if make > 0: # last round might not get time update
            tot += make 
        return tot
            

