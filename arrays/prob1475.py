# 1475. Final prices with a Special Discount in a shop

# 60% solution. not that good.
class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        finals = []
        m = len(prices)
        for i in range(m):
            p = prices[i]  # before discount
            for j in range(i+1, m):
                if prices[j] <= p:
                    p -= prices[j]
                    break
            finals.append(p)
        return finals

# 50% solution
class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        finals = []
        m = len(prices)
        for i in range(m):
            p = prices[i]  # before discount
            j = i + 1
            while j < m and prices[j] > p:
                j += 1
            if j < m:
                p -= prices[j]
            finals.append(p)
        return finals

