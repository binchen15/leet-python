# timelimit error. 135 / 138 test cases passed.
class Solution:
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        self.ans = 0
        
        def walk(path):
            
            i, j = path[-1]
            
            nbs = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            nbs = [ (x, y) for (x, y) in nbs if 0 <= x < m and 0 <= y < n \
                   and matrix[x][y] > matrix[i][j] ]
            if not nbs:  # good
                self.ans = max(self.ans, len(path))
                return
            
            for point in nbs:
                walk(path+[point])
                
        for i in range(m):
            for j in range(n):
                walk([(i,j)])
                
        return self.ans

# 30% solution
class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m = len(matrix)
        n = len(matrix[0])

        self.ans = 1

        @lru_cache(maxsize=None)
        def walk(i,j):
            res = 1
            nbs = [ (i+1,j), (i-1,j), (i,j+1), (i,j-1) ]
            nbs = [ (x, y) for (x, y) in nbs if 0 <= x < m and 0 <= y < n \
                   and matrix[x][y] > matrix[i][j] ]
            if not nbs:
                return res
            tmp = [1 + walk(*nb) for nb in nbs]
            return max(tmp)


        for i in range(m):
            for j in range(n):
                self.ans = max(self.ans, walk(i, j))

        return self.ans
