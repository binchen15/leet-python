class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [ [0] * n for _ in range(n) ]
        
        def helper(i0, m, v0):
            """fill the shell with topleft (i0, i0) and size m x m, start from v0
            return the next starting value for inner shell"""
            if m <= 0:
                return v0
            if m == 1:
                matrix[i0][i0] = v0
                return v0 + 1 # next value to start with
            
            v = v0
            for j in range(m):
                matrix[i0][i0+j] = v
                v += 1
            for i in range(1, m):
                matrix[i0+i][i0+m-1] = v
                v += 1
            for j in range(m-2,-1,-1):
                matrix[i0+m-1][i0+j] = v
                v += 1
            for i in range(m-2, 0, -1):
                matrix[i0+i][i0] = v 
                v += 1
                
            return v
                
        i0 = 0
        m  = n
        v0 = 1
        while v0 <= n * n: 
            v0 = helper(i0, m, v0)
            m -= 2
            i0 += 1
            
        return matrix
