# 474 ones and zeros

# defintion dp[i][j][k]: max strings formatted given j 0s, and k 1s 
# candidates up to strs[:i+1]
# dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-n0][k-n1])
# strs[i] have n0 0s, and n1 1s.
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        nr = len(strs)
        dp = [ [ [ 0 for k in range(n+1) ] 
                     for j in range(m+1) ] 
              for i in range(nr+1)]
        
        for i in range(1, nr+1):
            s  = strs[i-1]
            n0 = s.count('0')
            n1 = s.count('1')
            for j in range(0, m+1):
                for k in range(0, n+1):
                    if n0 <= j and n1 <= k:
                        dp[i][j][k] = max(
                            dp[i-1][j][k],
                            dp[i-1][j-n0][k-n1] + 1)
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
        return dp[nr][m][n]
    
# reduced space complexity
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        nr = len(strs)
        dp = [[ 0 for k in range(n+1) ] for j in range(m+1) ] 
             
        for i in range(nr):
            s  = strs[i]
            n0 = s.count('0')
            n1 = s.count('1')
            for j in range(m, n0-1, -1):
                for k in range(n, n1-1, -1):
                    dp[j][k] = max(
                        dp[j][k],
                        dp[j-n0][k-n1] + 1)
                    
        return dp[m][n]
    
