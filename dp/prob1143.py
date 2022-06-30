# 1143 Longest common subseqence

def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        if not m or not n:
            return 0

        #dp[i][j] for text1[:i+1] vs text2[:j+1]
        dp = [ [0] * (n+1) for _ in range(m+1) ]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)

        if m == 0 or n == 0:
            return 0

        memo = {}

        def helper(i, j):
            """text1[i:] vs text2[j:]"""

            if (i, j) in memo:
                return memo[(i, j)]

            if i >= m or j >= n:
                return 0

            if text1[i] == text2[j]:
                ans = 1 + helper(i+1, j+1)
            else:
                ans = max(helper(i, j+1), helper(i+1, j))

            memo[(i, j)] = ans
            return ans

        return helper(0, 0)
