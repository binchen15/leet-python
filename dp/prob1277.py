# 1277 Count Square Submatrices with all ones

class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        
        # number of square matrices ends at matrix[i][j]
        dp = [ [0] * n for _ in range(m) ]
        
        # init the first row and column
        for j in range(n):
            dp[0][j] = matrix[0][j]
        for i in range(1, m):
            dp[i][0] = matrix[i][0]
            
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                    
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += dp[i][j]
        return ans
                
