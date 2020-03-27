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
                

