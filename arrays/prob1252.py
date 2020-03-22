# 1252 Cells will odd values in a matrix

# 65%
class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        arr = [[0 for _ in range(m)] for _ in range(n)]
        # arr= [[0] *m] *n does not work. shallow copy?
        for r, c in indices:
            for j in range(m):
                arr[r][j] += 1
            for i in range(n):
                arr[i][c] += 1
        
        cnt = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] & 1:
                    cnt += 1
        return cnt
