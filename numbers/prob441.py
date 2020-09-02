# 441 Arranging Coins

# 30% solution
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n

        ans = 0    # answer to return
        left = n   # left number of coins
        width = 1  # width of next layer
        while width <= left:
            ans += 1
            left -= width
            width += 1
        return ans

# 70% solution
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        if n <= 1:
            return n

        k = int(math.sqrt(2*n) - 1)
        while (k+1)*(k+2) <= 2*n:
            k += 1
        return k
