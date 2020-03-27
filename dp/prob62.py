# 62 Unique Paths

# used a dp matrix
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [ [1] * n for _ in range(m)]
        for r in range(1, m):
            for c in range(1,n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[m-1][n-1]

# O(N) space complexity
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        prev = [1] * n
        curr = [1] * n
        for r in range(1, m):
            for c in range(1,n):
                curr[c] = prev[c] + curr[c-1]
            prev = curr
            curr = [1] * n
        return prev[-1]
                
# OMG. Crazy
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        curr = [1] * n
        for r in range(1, m):
            for c in range(1,n):
                curr[c] = curr[c] + curr[c-1]
        return curr[-1]
                
            

