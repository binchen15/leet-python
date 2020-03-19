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
                


