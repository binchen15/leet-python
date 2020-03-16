# 279 Perfect squares

# 50% dynamic programming solution.
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        # perfect square numbers allowed
        nums = [ i * i for i in range(1, int(math.sqrt(n)) + 1 )]
        dp = list(range(n+1)) # n = 1 + 1 + 1 + ... + 1. upper bound
        # dp[:4] is correct already
        for i in range(4, n+1):  # work on dp[i] using previous results
            for j in nums:
                if j <= i:
                    dp[i] = min(dp[i], 1 + dp[i-j])
                else:
                    break
        return dp[n]
