# 36 Valid Sudoku

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row = board[i]
            if not self.helper(row):
                return False
            col = [board[j][i] for j in range(9)]
            if not self.helper(col):
                return False
        for x in range(3):
            for y in range(3):
                dice = [ board[3*x+i][3*y+j] 
                        for i in range(3) 
                        for j in range(3) ]
                if not self.helper(dice):
                    return False
        return True
        
    def helper(self, nums):
        wc = set()
        for n in nums:
            if n != ".":
                if n in wc:
                    return False
                else:
                    wc.add(n)
        return True


