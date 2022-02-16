class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
        n = len(grid)

        xy = set()
        yz = set()
        zx = set()
        
        for x in range(n):
            for y in range(n):
                h = grid[x][y]
                for z in range(h):
                    xy.add((x, y))
                    yz.add((y, z))
                    zx.add((z, x))
                    
        return len(xy) + len(yz) + len(zx)
