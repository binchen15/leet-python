# 54. Sprial Matrix

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])
        if not n:
            return []
        
        ans = []
        i0  = 0  # rectangle, top-left,and bottom-right
        j0  = 0
        nr  = m
        nc  = n
        while i0 < nr and j0 < nc:
            top   = [matrix[i0][j]   for j in range(j0, nc) ]
            right = [matrix[i][nc-1] for i in range(i0+1, nr)]
            if nr-1 > i0:
                bottom = [matrix[nr-1][j] for j in range(nc-2, j0-1,-1) ]
            else:
                bottom = []
            if j0 < nc-1:
                left  = [matrix[i][j0]   for i in range(nr-2, i0, -1)]
            else:
                left = []
            ans.extend(top)
            ans.extend(right)
            ans.extend(bottom)
            ans.extend(left)
            i0 += 1
            j0 += 1
            nr -= 1
            nc -= 1
        return ans
        
