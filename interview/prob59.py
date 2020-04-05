# 59. Spiral Matrix II

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[1]]
        
        matrix = [ [0] * n for _ in range(n)]
        i0, j0 = 0, 0
        nr, nc = n, n
        cnt = 0
        while i0 < nr and j0 < nc:
            # top, right, bottom, left
            for j in range(j0, nc):
                cnt += 1
                matrix[i0][j] = cnt
            for i in range(i0+1, nr):
                cnt += 1
                matrix[i][nc-1] = cnt
            for j in range(nc-2, j0-1, -1):
                cnt += 1
                matrix[nr-1][j] = cnt
            for i in range(nr-2, i0, -1):
                cnt += 1
                matrix[i][j0] = cnt
            i0 += 1
            j0 += 1
            nr -= 1
            nc -= 1
                
        return matrix
                
            
