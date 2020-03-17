# 695 max area of island

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nr = len(grid)
        nc = len(grid[0])
        # 1 means island, and not visited yet
        mask = [ [ grid[i][j]  for j in range(nc) ] for i in range(nr) ]
        ans = 0

        for i in range(nr):
            for j in range(nc):
                if mask[i][j]:
                    ans = max(ans, self.areaOfNode(grid, nr, nc, i, j, mask))
        return ans

    # stuck. when to put on the mask?

    def areaOfNode(self, grid, nr, nc, i, j, mask):
        """(i,j) must be within grid, and be island itself"""
        if i < 0 or i >= nr or \
           j < 0 or j >= nc or \
           grid[i][j] == 0:
            return 0
        area = 1
        mask[i][j] = 0
        nbs  = self.findNeighbors(grid, nr, nc, i, j, mask)
        if not nbs:
            return area
        else:
            for nb in nbs:
                #mask[nb[0]][nb[1]] = 1
                area += self.areaOfNode(grid, nr, nc, nb[0], nb[1], mask)
            return area


    def findNeighbors(self, grid, nr, nc, i, j, mask):
        nbs = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        ans = filter(lambda p: 0 <= p[0] and p[0] < nr and \
                               0 <= p[1] and p[1] < nc and \
                               mask[p[0]][p[1]], nbs)
        for i, j in ans:
            mask[i][j] = 0
        return ans

# same as above. slightly cleaned.
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nr = len(grid)
        nc = len(grid[0])

        # 1 means island not visited yet 1->0 if visited already
        mask = [ [ grid[i][j]  for j in range(nc) ] for i in range(nr) ]

        ans = 0
        for i in range(nr):
            for j in range(nc):
                if mask[i][j]:
                    mask[i][j] = 0
                    ans = max(ans, self.areaOfNode(grid, nr, nc, i, j, mask))
        return ans

    def areaOfNode(self, grid, nr, nc, i, j, mask):
        """(i,j) must be within grid, and be island itself"""
        #if i < 0 or i >= nr or \
        #   j < 0 or j >= nc or \
        #   grid[i][j] == 0:
        #    return 0
        area = 1
        nbs  = self.findNeighbors(grid, nr, nc, i, j, mask)
        if not nbs:
            return area
        else:
            for nb in nbs:
                area += self.areaOfNode(grid, nr, nc, nb[0], nb[1], mask)
            return area


    def findNeighbors(self, grid, nr, nc, i, j, mask):
        nbs = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        ans = filter(lambda p: 0 <= p[0] and p[0] < nr and \
                               0 <= p[1] and p[1] < nc and \
                               mask[p[0]][p[1]], nbs)
        for i, j in ans:
            mask[i][j] = 0
        return ans

# removed the mask matrix. change grid in-place. 
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nr = len(grid)
        nc = len(grid[0])
        
        ans = 0      
        for i in range(nr):
            for j in range(nc):
                if grid[i][j]:
                    grid[i][j] = 0
                    ans = max(ans, self.areaOfNode(grid, nr, nc, i, j))
        return ans
        
    def areaOfNode(self, grid, nr, nc, i, j):
        """(i,j) must be within grid, and be island itself"""
        #if i < 0 or i >= nr or \
        #   j < 0 or j >= nc or \
        #   grid[i][j] == 0:
        #    return 0
        area = 1
        nbs  = self.findNeighbors(grid, nr, nc, i, j)
        if not nbs:
            return area
        else:
            for nb in nbs:
                area += self.areaOfNode(grid, nr, nc, nb[0], nb[1])
            return area
            
    def findNeighbors(self, grid, nr, nc, i, j):
        nbs = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        ans = filter(lambda p: 0 <= p[0] and p[0] < nr and \
                               0 <= p[1] and p[1] < nc and \
                               grid[p[0]][p[1]], nbs)
        for i, j in ans:
            grid[i][j] = 0
        return ans
