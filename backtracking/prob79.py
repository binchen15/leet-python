# 79. Word Search

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        nr = len(board)
        nc = len(board[0])
        m  = len(word)
        mask = [[True for j in range(nc)] for i in range(nr)]
        
        for i in range(nr):
            for j in range(nc):
                if board[i][j] == word[0]:
                    chars = [(i,j)]
                    mask[i][j] = False  
                    if self.backtrack(board, nr, nc, m, chars, word[1:], mask):
                        return True
                    else:
                        mask[i][j] = True    
                    
        return False   
        
    def backtrack(self, board, nr, nc, m, chars, word, mask):
        if len(chars) == m or not len(word):
            return True
 
        p,q = chars[-1]
        nb4 = [(p-1,q),(p+1,q),(p,q-1),(p,q+1)]
        nbs = filter(lambda x: 0 <= x[0] and x[0] < nr and \
                               0 <= x[1] and x[1] < nc and \
                               board[x[0]][x[1]] == word[0] and \
                               mask[x[0]][x[1]], nb4)
        if not nbs:
            return False
        else:
            for u,v in nbs:
                chars.append((u,v))
                mask[u][v] = False
                flag = self.backtrack(board, nr, nc, m, chars, word[1:], mask)
                if flag:
                    return True
                else:
                    chars.pop()
                    mask[u][v] = True
            return False
                

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        l = len(word)
        
        if l > m*n:
            return False
        
        track = [ [0] * n for _ in range(m) ]  # 0, 1 means unwalked, walked
        
        def walk(i, row, col):
            """word[i] to be walked at (row, col), track[row][col] set to 1 already"""
            
            if board[row][col] != word[i]:
                return False
            
            if i == l-1:
                return True
            
            nbrs = [ [row+1, col], [row-1, col], [row, col+1], [row, col-1] ]
            nbrs = [(r,c) for r, c in nbrs if 0 <= r < m and 0 <= c < n and track[r][c] == 0]
            if not nbrs:
                return False
            
            for (r, c) in nbrs:
                track[r][c] = 1
                if walk(i+1, r, c):
                    return True
                track[r][c] = 0
            
            return False
        
        for r in range(m):
            for c in range(n):
                track[r][c] = 1
                if walk(0, r, c):
                    return True
                track[r][c] = 0
                
        return False
    
