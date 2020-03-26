# 1275 Tic Tac Toe

class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        board = [ [" "," "," "] for _ in range(3)]
        for i, move in enumerate(moves):
            x, y = move
            if i & 1:  
                board[x][y] = "O"
            else:
                board[x][y] = "X"
                
        for i in range(3):
            rc = board[i][0] == board[i][1] and \
                 board[i][1] == board[i][2]
            cc = board[0][i] == board[1][i] and \
                 board[1][i] == board[2][i]
            if rc:
                if board[i][0] == "X":
                    return "A"
                elif board[i][0] == "O":
                    return "B"
            if cc:
                if board[0][i] == "X":
                    return "A"
                elif board[0][i] == "O":
                    return "B"
                
        if board[0][0] == board[1][1] and \
           board[1][1] == board[2][2]:
            if board[0][0] == "X":
                return "A"
            elif board[0][0] == "O":
                    return "B"
        if board[0][2] == board[1][1] and \
           board[1][1] == board[2][0]:
            if board[0][2] == "X":
                return "A"
            elif board[0][2] == "O":
                return "B"
        
        for row in board:
            if " " in row:
                return "Pending"
        return "Draw"
                
          
