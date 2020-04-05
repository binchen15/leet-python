# 74 Search 2D matrix

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if not m:
            return False
        n = len(matrix[0])
        if not n:
            return False
        
        if target < matrix[0][0] or \
           target > matrix[m-1][n-1]:
            return False
        
        # last column. find which row to do bisect
        lc = [ matrix[i][n-1] for i in range(m) ]
        l, h = 0, m-1
        while l <= h:
            mid = l + (h-l)//2
            if lc[mid] == target:
                return True
            elif lc[mid] > target:
                h = mid - 1
            else:
                l = mid + 1
                
        # test the row l now
        if n == 1:
            return False
        
        row  = matrix[l]  # l the row index
        l, h = 0, n-1
        while l <= h:
            mid = l + (h-l)//2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                h = mid - 1
            else:
                l = mid + 1
        return False        
        
        
