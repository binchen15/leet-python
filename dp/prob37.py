# 37 Sudoku solver
        
# 60% solution
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        seq = []  # (i,j) of empty cells
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    seq.append((i,j))
        n = len(seq)
        if n == 0: # nothing to do
            return 
        # assume one and only one solution exists
        self.traverse(0, seq, board)
        return
    
    def traverse(self, k, seq, board):
        """k mean numbers of holes filled up so far"""
        if k == len(seq):
            return True
        i, j = seq[k] # (i, j) needs be filled
        choices = self.candidates(board, i, j)
        if not choices:  # dead end
            return False
        for choice in choices:
            board[i][j] = choice
            flag = self.traverse(k+1, seq, board)
            if flag:
                return True
            else:
                board[i][j] = "."
        return False
            
    def candidates(self, board, i, j):
        row = board[i]
        col = [ board[r][j] for r in range(9) ]
        X = i // 3
        Y = j // 3
        dice = [ board[3*X+i][3*Y+j] for i in range(3) for j in range(3)]
        used = set(row+col+dice)
        return [ str(i) for i in range(1,10) if str(i) not in used]
         
