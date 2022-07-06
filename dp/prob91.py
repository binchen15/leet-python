# 91 Decode Ways

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.startswith("0"):
            return 0
        m  = len(s)
        dp = [0] * m
        dp[0] = 1
        for i in range(1, m):
            d = int(s[i])
            if d == 0: # must combine with previous digit
                n = int(s[i-1:i+1])
                if n == 0 or n > 26:
                    dp[i] = 0
                else:
                    if i-2 >= 0:
                        dp[i] = dp[i-2]
                    else:
                        dp[i] = 1
            else:
                # at least dp[i-1]  # by itself, one scenario
                n = int(s[i-1:i+1])
                if n < 10 or n > 26: # can not combine with previous digit
                    dp[i] = dp[i-1]
                else:
                    if i-2 >= 0:
                        dp[i] = dp[i-2] + dp[i-1]
                    else:
                        dp[i] = 1 + dp[i-1]
            
        return dp[m-1]            
                

# recursion with memoization
class Solution:

    @lru_cache(maxsize=None)
    def numDecodings(self, s: str) -> int:

        if not s:
            return 1

        if s.startswith("0"):
            return 0

        n = len(s)
        if n == 1:
            return 1

        numbers = set(str(i) for i in range(1, 27))
        digits = set(str(i) for i in range(1, 10))

        ans = 0
        if s[n-1] in digits:
            ans +=  self.numDecodings(s[:n-1])
        if s[n-2:] in numbers:
            ans += self.numDecodings(s[:n-2])

        return ans

# DP 
class Solution:

    def numDecodings(self, s: str) -> int:

        n = len(s)
        digits = set(str(i) for i in range(1, 10))
        numbers = set(str(i) for i in range(1, 27))

        dp = [0] * (n+1)
        dp[0] = 1
        if s[0] != "0":
            dp[1] = 1

        for i in range(2, n+1):
            c1 = s[i-1]
            c2 = s[i-2:i]
            if c1 in digits:
                dp[i] += dp[i-1]
            if c2 in numbers:
                dp[i] += dp[i-2]

        return dp[n]
