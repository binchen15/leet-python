# 1260 shift 2D grid

class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        for _ in range(k):
            self.shift(grid)
        return grid
            
    def shift(self, grid):
        """shift grid one step"""
        nr = len(grid)
        nc = len(grid[0])
        first = grid[nr-1][nc-1]
        for r in range(nr):
            first = self.shiftRow(grid[r], first)
            
        
    def shiftRow(self, row, first):
        m = len(row)
        last = row[-1]
        for i in range(m-1, 0, -1):
            row[i] = row[i-1]
        row[0] = first
        return last
            
