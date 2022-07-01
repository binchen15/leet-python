class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        
        m = len(s)
        n = len(t)
        
        dp = [ [0] * (n+1) for _ in range(m+1) ]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    
        dp2 = [ [0] * (n+1) for _ in range(m+1) ]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == t[j]:
                    dp2[i][j] = 1 + dp2[i+1][j+1]
                    
        ans = 0
        for i in range(m):
            for j in range(n):
                if s[i] != t[j]:
                    ans += (1+ dp[i][j]) * (1 + dp2[i+1][j+1])
                    
        return ans
