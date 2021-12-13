# 200 number of islands

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        nr = len(grid)
        if not nr:
            return 0
        nc = len(grid[0])
        if not nc:
            return 0

        cnt = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':  # new island
                    cnt += 1
                    grid[i][j] = '0'
                    self.expand(grid, nr, nc, i, j)
        return cnt

    def expand(self, grid, nr, nc, i, j):
        """erase all reachable areas"""
        nbs = [ (i-1,j), (i+1,j), (i,j-1), (i,j+1)]
        ans = filter(lambda p:  0 <= p[0] and  p[0] < nr and \
                                0 <= p[1] and  p[1] < nc and \
                                grid[p[0]][p[1]] == '1', nbs)
        for u, v in ans:
            grid[u][v] = '0' # erase it
        for u, v in ans:
            self.expand(grid, nr, nc, u, v)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        def walk(x, y):
            """walk the island from (i,j) assuming grid[i][j]=1"""
            
            cur = [(x, y)]
            nxt = []
            while True:
                while cur:
                    i, j = cur.pop(0)
                    grid[i][j] = 0
                    nbrs = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                    nbrs = [(i, j) for i, j in nbrs if 0 <= i < m and 0 <= j < n and grid[i][j] == "1"]
                    for a, b in nbrs:
                        grid[a][b] = 0
                        nxt.append((a,b))
                if nxt:
                    cur = nxt
                    nxt = []
                else:
                    break
                    
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    walk(i, j)
                    
        return ans
        

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])

        def walk(i, j):
            """walk the island from (i,j) assuming grid[i][j]=1"""
            grid[i][j] = "0"
            nbrs = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            nbrs = [(i, j) for i, j in nbrs if 0 <= i < m and 0 <= j < n and grid[i][j] == "1"]
            for x, y in nbrs:
                walk(x, y)

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    walk(i, j)

        return ans

