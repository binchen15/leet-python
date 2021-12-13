class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        def walk():
            
            minutes = 0
            cnts = []
            while True:
                to_rot = set()
                for i in range(m):
                    for j in range(n):
                        if grid[i][j] == 0:
                            continue
                        elif grid[i][j] == 1:
                            continue

                        if grid[i][j] == 2:
                            nbrs = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                            nbrs = [(i, j) for (i, j) in nbrs if 0 <= i < m and 0 <= j < n and grid[i][j] == 1]
                            to_rot.update(nbrs)
                            
                if len(to_rot) == 0:
                    break
                else:
                    minutes += 1
                    cnts.append(len(to_rot))
                    for x, y in to_rot:
                        grid[x][y] = 2
            
            return [minutes, cnts]
        
        fresh_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                    
        minutes, cnts = walk()
        # print(cnts)
        if fresh_count > sum(cnts):
            return -1
        else:
            return minutes

