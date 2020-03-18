# 417. Pacific Atlantic Water Flow

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        nr = len(matrix)
        if not nr:
            return []
        nc = len(matrix[0])
        if not nc:
            return []
        
        pacific  = [[ False for j in range(nc)] for i in range(nr)]
        atlantic = [[ False for j in range(nc)] for i in range(nr)]
        
        for j in range(nc):
            self.expand(matrix, nr, nc, 0,    j, pacific)
            self.expand(matrix, nr, nc, nr-1, j, atlantic)
            
        for i in range(nr):
            self.expand(matrix, nr, nc, i,    0, pacific)
            self.expand(matrix, nr, nc, i, nc-1, atlantic)
            
        ans = []
        for i in range(nr):
            for j in range(nc):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i,j])
        return ans
        
    def expand(self, matrix, nr, nc, i, j, mask):
        if mask[i][j]:
            return
        mask[i][j] = True
        nbs  = [(i-1,j), (i+1,j), (i,j-1),(i,j+1)]
        gnbs = filter(lambda p :
                      0 <= p[0] and p[0] < nr and \
                      0 <= p[1] and p[1] < nc and \
                      matrix[p[0]][p[1]] >= matrix[i][j],
                      nbs)
        for p,q in gnbs:  # good neighbors
            self.expand(matrix, nr, nc, p, q, mask)
