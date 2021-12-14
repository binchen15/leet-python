class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        if n <= 1:
            return n
        
        dp = [ [0] * n for _ in range(n) ]
        
        for i in range(n):
            dp[i][i] = 1
            
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
            
        for delta in range(2, n):
            for i in range(n-delta):
                if dp[i+1][i+delta-1] == 1 and s[i] == s[i+delta]:
                    dp[i][i+delta] = 1

        ans = sum([sum(row) for row in dp])
        return ans

