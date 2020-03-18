# 130 surrounded region

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        nr = len(board)
        if not nr:
            return
        nc = len(board[0])
        if not nc:
            return
        
        # true means pixels connected to boundary, uncapturable
        mask = [ [ False for c in range(nc)] for r in range(nr)]
        
        for j in range(nc):
            for i in (0, nr-1):
                if board[i][j] == "O":
                    self.expand(board, nr, nc, i, j, mask)
                
        for i in range(1, nr-1): # second the next to last row
            for j in (0, nc-1):
                if board[i][j] == "O":
                    self.expand(board, nr, nc, i, j, mask)
                
        for i in range(nr):
            for j in range(nc):
                if not mask[i][j]: # not connected to boundary
                    board[i][j] = 'X'
        return
                
        
    def expand(self, board, nr, nc, i, j, mask):
        """start from (i,j), mask connected regions,
        (i,j) supposed to be on the bounary"""
        if mask[i][j]:  # already masked. bad pixel
            return
        mask[i][j] = True
        nbs   = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
        reals = filter( lambda p:
            0 <= p[0] and p[0] < nr and \
            0 <= p[1] and p[1] < nc and \
            board[p[0]][p[1]] == 'O',
            nbs)
        for p, q in reals:
            self.expand(board, nr, nc, p, q, mask)
            
       
