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

# July 4 2022 TimeLimit error 218/231
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        n = len(s)
        ans = 0
        dp = [ [0] * n for _ in range(n) ]

        for i in range(n-1):
            if s[i:i+2] == "()":
                dp[i][i+1] = 1
                ans = 2

        for delta in range(3, n, 2):
            for i in range(n-delta):
                j = i + delta
                if s[i] == "(" and s[j] == ")" and dp[i+1][j-1] == 1:
                    dp[i][j] = 1
                else:
                    for k in range(i+1, j-1, 2):
                        if dp[i][k] == 1 and dp[k+1][j] == 1:
                            dp[i][j] = 1
                            break
                if dp[i][j] == 1:
                    ans = j-i+1

        return ans

# 221/231 passed
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        n = len(s)
        ans = 0
        dp = [ [0] * n for _ in range(n) ]

        for i in range(n-1):
            if s[i:i+2] == "()":
                dp[i][i+1] = 1
                ans = 2

        for delta in range(3, n, 2):
            for i in range(n-delta):
                j = i + delta
                if not ( s[i] == "(" and s[j] == ")" ):
                    continue
                if dp[i+1][j-1] == 1:
                    dp[i][j] = 1
                else:
                    for k in range(i+1, j-1, 2):
                        if dp[i][k] == 1 and dp[k+1][j] == 1:
                            dp[i][j] = 1
                            break
                if dp[i][j] == 1:
                    ans = j-i+1

        return ans

# repeat old 1D DP works
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        n = len(s)
        if n <= 1:
            return 0
        dp = [0] * n

        if s[:2] == "()":
            dp[1] = 2

        for i in range(2, n):
            if s[i] == "(":
                continue
            if s[i-1] == "(":
                dp[i] = 2 + dp[i-2]
            else:
                if dp[i-1] == 0:
                    dp[i] == 0
                else:
                    m = dp[i-1]
                    if i-1-m >= 0 and s[i-1-m] == "(":
                        dp[i] = dp[i-1] + 2
                        if   i-1-m > 0:
                            dp[i] += dp[i-1-m-1]
                    else:
                        dp[i] = 0

        return max(dp)
