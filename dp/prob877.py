# recurision + memo  30% solution
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        n = len(piles)

        @lru_cache(maxsize=None)
        def helper(i, j):
            """piles[i:j+1]"""
            if j == i + 1:
                return abs(piles[i] - piles[j])

            c1 = piles[i] - piles[j] + helper(i+1, j-1)
            c2 = piles[j] - piles[i] + helper(i+1, j-1)
            c3 = piles[i] - piles[i+1] + helper(i+2, j)
            c4 = piles[j] - piles[j-1] + helper(i, j-2)

            return max(c1,c2,c3,c4)

        return helper(0, n-1) > 0

# dp solution 5%
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        n = len(piles)
        if n == 2:
            return True
        
        dp = [ [0] * n for _ in range(n) ]
        for i in range(0, n-1):
            dp[i][i+1] = abs(piles[i] - piles[i+1])
            
        for delta in range(2, n):
            for i in range(0, n-delta):
                j = i + delta
                c1 = piles[i] - piles[j] + dp[i+1][j-1]
                c2 = piles[j] - piles[i] + dp[i+1][j-1]
                c3 = piles[i] - piles[i+1] + dp[i+2][j]
                c4 = piles[j] - piles[j-1] + dp[i][j-2]

                dp[i][j] = max(c1,c2,c3,c4)
        
        return dp[0][n-1] > 0


