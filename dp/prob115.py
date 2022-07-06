# distinct subsequences
class Solution:

    @lru_cache(maxsize=None)
    def numDistinct(self, s: str, t: str) -> int:

        m = len(s)
        n = len(t)
        if m < n:
            return 0
        if m == n:
            return 1 if s == t else 0

        if n == 0:
            return 1

        if s[-1] != t[-1]:
            return self.numDistinct(s[:m-1], t)
        else:
            return self.numDistinct(s[:m-1], t) + self.numDistinct(s[:m-1], t[:n-1])

# DP solution
class Solution:

    def numDistinct(self, s: str, t: str) -> int:

        m = len(s)
        n = len(t)
        if m < n:
            return 0
        if m == n:
            return 1 if s == t else 0

        if n == 0:
            return 1

        dp = [ [0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] != t[j-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

        return dp[m][n]
