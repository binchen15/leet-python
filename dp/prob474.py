# knapsack strategy 5% solution
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        h = len(strs)
        
        dp = [ [ [0] * (n+1) for _ in range(m+1) ]  for _ in range(h+1)]
        
        for k in range(1, h+1):
            s = strs[k-1]
            zeros = s.count("0")
            ones = s.count("1")
            
            for i in range(0, m+1):
                for j in range(0, n+1):
                    if i == 0 and j == 0:
                        continue
                    i0, j0 = i - zeros, j - ones
                    if i0 < 0 or j0 < 0:  # strs[k] is useless
                        dp[k][i][j] = dp[k-1][i][j]
                    else:
                        dp[k][i][j] = max(
                            1 + dp[k-1][i0][j0], 
                            dp[k-1][i][j]
                        )
                         
        return dp[h][m][n]
