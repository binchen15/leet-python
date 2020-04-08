# 85. Maximal Rectangle

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if not m:
            return 0
        n = len(matrix[0])
        if not n:
            return 0
                
        dp1 = [ [0] * n for _ in range(m)] # 1s to the left of matrix[i][j]
        dp3 = [ [0] * n for _ in range(m)] # 1s above matrix[i][j]
        dp2 = [ [ [0, 0] for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            dp1[i][0] = int(matrix[i][0])
        for j in range(n):
            dp3[0][j] = int(matrix[0][j])
        
        for i in range(m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp1[i][j] = dp1[i][j-1] + 1 
                    
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp3[i][j] = dp3[i-1][j] + 1 
        
        for j in range(n):
            if matrix[0][j] == '1':
                dp2[0][j] = [dp1[0][j], 1]
        
        for i in range(1, m):
            if matrix[i][0] == '1':
                dp2[i][0] = [1, dp3[i][0]]
                
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    l1 = dp1[i][j]
                    w3 = dp3[i][j]
                    if l1 >= w3:
                        pair = [l1, 1]
                    else:
                        pair = [1, w3]
                    if matrix[i-1][j] == '1':
                        l2, w = dp2[i-1][j]
                        tmp = [min(l1, l2), w+1]
                        if tmp[0] * tmp[1] > pair[0]*pair[1]:
                            pair = tmp
                    if matrix[i][j-1] == '1':
                        l2, w = dp2[i][j-1]
                        tmp = [l2+1, min(w, w3)]
                        if tmp[0] * tmp[1] > pair[0]*pair[1]:
                            pair = tmp
                    dp2[i][j] = pair
                    
        ans = 0
        for i in range(m):
            for j in range(n):
                pix = dp2[i][j]
                ans = max(ans, pix[0]*pix[1])    
        return ans
        
