#64 Minimum path sum

# key observation: dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c]
# first row/column are deterministic
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nr = len(grid)
        nc = len(grid[0])
        dp = [ [0] * nc for _ in range(nr) ]
        dp[0][0] = grid[0][0]
        for c in range(1, nc):
            dp[0][c] = dp[0][c-1] + grid[0][c]
        for r in range(1, nr):
            dp[r][0] = dp[r-1][0] + grid[r][0]
        for r in range(1, nr):
            for c in range(1, nc):
                dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c]    
        return dp[nr-1][nc-1]
