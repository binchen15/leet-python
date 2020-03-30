# 1314 Matrix Block Sum

class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        ans = [ [0] * n for _ in range(m) ]
        ans[0][0] = self.blockSum(mat, m, n, K, 0, 0)
        for j in range(1, n):
            ans[0][j] = ans[0][j-1] + self.dc1(mat, m, n, K, 0, j-1)
        for i in range(1, m):
            for j in range(n):
                ans[i][j] = ans[i-1][j] + self.dr1(mat, m, n, K, i-1, j)
        return ans
        
        
    def blockSum(self, mat, m, n, K, x, y):
        tot = 0
        for i in range(x-K, x+K+1):
            if 0 <= i and i < m:
                for j in range(y-K, y+K+1):
                    if 0 <= j and j < n:
                        tot += mat[i][j]
        return tot
    
    def dc1(self, mat, m, n, K, x, y):
        """difference in block sum when shift the block centered (x,y) 
          1 unit to the right"""
        tot = 0
        c1 = y - K
        c2 = y + K + 1
        if 0 <= c1 and c1 < n:
            for i in range(x-K, x+K+1):
                if 0 <= i and i < m:
                    tot -= mat[i][c1]
        if 0 <= c2 and c2 < n:
            for i in range(x-K, x+K+1):
                if 0 <= i and i < m:
                    tot += mat[i][c2]
        return tot
                    
    def dr1(self, mat, m, n, K, x, y):
        """difference in block sum when shift the block 
           centered (x,y) 1 unit to the bottom"""
        tot = 0
        r1 = x - K
        r2 = x + K + 1
        if 0 <= r1 and r1 < m:
            for j in range(y-K, y+K+1):
                if 0 <= j and j < n:
                    tot -= mat[r1][j]
        if 0 <= r2 and r2 < m:
            for j in range(y-K, y+K+1):
                if 0 <= j and j < n:
                    tot += mat[r2][j]
        return tot
                    
    
                    
                  
