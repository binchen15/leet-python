
# recursion + memo
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)
        if n <= 1:
            return n

        memo = {}

        def helper(i, j):
            """ work on s[i:j+1] """
            if i > j:
                return 0
            if i == j:
                return 1

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == s[j]:
                ans = 2 + helper(i+1, j-1)
            else:
                ans = max(helper(i, j-1), helper(i+1, j))
            memo[(i,j)] = ans
            return ans

        return helper(0, n-1)


# dp solution
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)
        if n <= 1:
            return n

        # dp[i][j] for s[i:j+1]
        dp = [ [0] * n for _ in range(n) ]

        for i in range(n):
            dp[i][i] = 1

        for delta in range(1, n):
            for i in range(n-delta):
                j = i + delta
                if j == i + 1:
                    dp[i][j] = 2 if s[i] == s[j] else 1 # 1 not 0
                else:
                    if s[i] == s[j]:
                        dp[i][j] = 2 + dp[i+1][j-1]
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])


        return dp[0][n-1]
