# 1091 shortest path in binary matrix

# 40% in speed
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid) # dimension of the grid
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        currL = [(0,0)]
        nextL = []
        level = 0
        grid[0][0] = 1
        while currL:
            level += 1
            while currL:
                i,j = currL.pop(0) # current cell
                if (i,j) == (n-1, n-1):
                    return level
                candidates = [
                    (i-1,j),(i+1,j),(i,j-1),(i,j+1),
                    (i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]
                for p in candidates:
                    if 0 <= p[0] and p[0] < n and \
                       0 <= p[1] and p[1] < n and \
                       grid[p[0]][p[1]] == 0:
                        nextL.append(p)
                        grid[p[0]][p[1]] = 1
            currL = nextL
            nextL = []
        return -1                
                
                
        
