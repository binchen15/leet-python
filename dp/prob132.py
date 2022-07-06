class Solution:
    def minCut(self, s: str) -> int:
        
        n = len(s)
        if n <= 1:
            return 0
        
        dp = [ [0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            
        for delta in range(1, n):
            for i in range(n-delta):
                j = i + delta
                # s[i:j+1]
                if s[i] == s[j]:
                    if j == i+1 or j == i+2 or dp[i+1][j-1] == 1:
                        dp[i][j] = 1
                        
        @lru_cache(maxsize=None)
        def helper(i, j):
            """minimum cuts to make s[i:j+1] palindromes"""
            if j == i:
                return 0
            if dp[i][j] == 1:
                return 0
            
            arr = []
            for k in range(i, j):
                if dp[i][k] == 1: # s[i:k+1] vs s[k+1:j+1]
                    arr.append(1 + helper(k+1, j))
                    
            return min(arr)
        
        ans = helper(0, n-1)
        return ans
