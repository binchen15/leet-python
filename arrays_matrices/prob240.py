class Solution(object):
    """40% solution, row by row bisection algorithm"""
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        nr = len(matrix)
        if nr == 0:
            return False
        nc = len(matrix[0])
        if nc == 0:
            return False
        for i in range(nr):
            if target < matrix[i][0] or \
               target > matrix[i][nc-1]:
                continue
            flag = self.find(matrix[i], target)
            if flag:
                return True
        return False
    
    def find(self, row, target):
        m = len(row)
        l, h = 0, m - 1
        while l <= h:
            mid = l + (h-l)//2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                h = mid - 1
            else:
                l = mid + 1
        return False

class Solution(object):
    """95% solution"""
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        nr = len(matrix)
        if nr == 0:
            return False
        nc = len(matrix[0])
        if nc == 0:
            return False
        row = 0         # start from top right corner
        col = nc - 1
        
        while row < nr and col >= 0:
            val = matrix[row][col] 
            if val == target:
                return True
            elif target < val:
                col -= 1
            else:
                row += 1
        return False
        
