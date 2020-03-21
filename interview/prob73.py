# 73. Set matrix zeros

# O(m+n) space complexity
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        nr = len(matrix)
        nc = len(matrix[0])

        rows = []
        cols = []
        for i in range(nr):
            for j in range(nc):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        for r in rows:
            for j in range(nc):
                matrix[r][j] = 0

        for j in cols:
            for i in range(nr):
                matrix[i][j] = 0

# O(1) space complexity solution
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        nr = len(matrix)
        nc = len(matrix[0])
        
        r0 = False
        c0 = False
        
        for i in range(nr):
            for j in range(nc):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i == 0:
                        r0 = True
                    if j == 0:
                        c0 = True
                    
        for i in range(1,nr):
            if matrix[i][0] == 0:
                for j in range(nc):
                    matrix[i][j] = 0
                
        for j in range(1,nc):
            if matrix[0][j] == 0:
                for i in range(nr):
                    matrix[i][j] = 0
                
        if r0:
            for j in range(nc):
                matrix[0][j] = 0
        if c0:
            for i in range(nr):
                matrix[i][0] = 0
                
                
