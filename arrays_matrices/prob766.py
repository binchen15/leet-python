# Toeplitz Matrix
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        nr = len(matrix)
        nc = len(matrix[0])
        
        # starting from first row
        for c in range(nc-1):
            i = 0 # start from first row
            j = c
            v = matrix[i][j]
            while i < nr and j < nc:
                if matrix[i][j] != v:
                    return False
                else: # walk in the diagnal direction
                    i += 1
                    j += 1
        for r in range(1, nr-1):
            i = r
            j = 0
            v = matrix[i][j]
            while i < nr and j < nc:
                if matrix[i][j] != v:
                    return False
                else: # walk in the diagnal direction
                    i += 1
                    j += 1
                
        return True
                
        
