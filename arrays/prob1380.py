# 1380 Lucky Numbers in a matrix

class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            row = matrix[i]
            c = row.index(min(row))
            val = matrix[i][c]
            lucky = True
            for r in range(m):
                if matrix[r][c] > val:
                    lucky = False
                    break
            if lucky:
                ans.append(val)
        return ans
            
