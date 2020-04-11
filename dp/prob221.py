# 221 Maximal Square

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if not m:
            return 0
        n = len(matrix[0])
        if not n:
            return 0
        
        dp = [ [ 0 ] * n for _ in range(m)]
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
        for i in range(1, m):
            dp[i][0] = int(matrix[i][0])
            
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j-1],
                                      dp[i-1][j])

        #print(dp)      
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dp[i][j])
        return ans*ans
                    
