# 343 Integer Break

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(3, n+1):
            m = 0
            for a in range(1, i//2+1):
                b = i - a
                c = max(a, dp[a])*max(b, dp[b])
                m = max(m, c)
            dp[i] = m
        return dp[n]
