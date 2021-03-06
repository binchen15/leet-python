# 1351 Count Negative Numbers in a sorted matrix

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt = 0
        nr = len(grid)
        nc = len(grid[0])
        imax = nr
        jmax = nc
        i = 0
        while i < imax:
            j = 0
            while j < jmax:
                if grid[i][j] < 0:
                    cnt += (imax - i) * (jmax - j)
                    jmax = j
                    break
                j += 1
            i += 1
        return cnt
                    
                
