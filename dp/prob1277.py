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
                
# July 1 2022
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        if m < 1 or n < 1:
            return 0
        
        ans = 0
        
        # dp[i][j] store the size of the largest square ends on it
        dp = [ [0] * (n+1) for _ in range(m+1) ]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                    ans += dp[i][j]
                    
                    
        return ans
