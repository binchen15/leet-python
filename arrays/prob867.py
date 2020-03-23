# 867 Transpose Matrix

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B  = []
        nr = len(A)
        nc = len(A[0])
        for c in range(nc):
            row = [A[r][c] for r in range(nr)]
            B.append(row)
        return B
                
