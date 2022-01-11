class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    
        m = len(grid)
        n = len(grid[0])
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    grid[i][j] == "0"
                    self.walk(grid, i, j, m, n)
                    
        return ans
        
        
    def walk(self, grid, i, j, m, n):
        "assume (i, j) = 1, erase the island"
        cur = [(i,j)]
        nxt = []
        while True:
            while cur:
                i, j = cur.pop(0)
                nbrs = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                nbrs = [(x, y) for (x, y) in nbrs if 0 <= x < m and 0 <= y < n and grid[x][y] == "1"]
                for x, y in nbrs:
                    grid[x][y] = "0"
                nxt.extend(nbrs)
            if not nxt:
                break
            else:
                cur = nxt
                nxt = []
