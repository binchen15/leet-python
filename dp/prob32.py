# 32 Longest Valid Parentheses

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = len(s)
        if m <= 1:
            return 0

        # longest valid parentheses ends at dp[i]
        dp = [0] * m
        if s[0] == "(" and s[1] == ")":
            dp[1] = 2
        else:
            dp[1] = 0
        for i in range(2, m):
            if s[i] == "(":  # can not end at openning
                dp[i] = 0
            else:  # s[i] == ")" can I close something?
                if s[i-1] == "(":
                    dp[i] = 2
                    if i-2 >= 0:
                        dp[i] += dp[i-2]
                else: # s[i-1] == ")"
                    if dp[i-1] == 0:
                        dp[i] = 0
                    else: # previous is closed
                        tmp = dp[i-1]
                        if i-1-tmp >= 0 and s[i-1-tmp] == "(":
                            dp[i] = dp[i-1] + 2
                            if i-1-tmp-1 >= 0:
                                dp[i] += dp[i-1-tmp-1]
                        else:
                            dp[i] = 0
        return max(dp)
                        
