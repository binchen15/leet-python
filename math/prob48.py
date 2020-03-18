# 48 rotate image

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 1:
            return
        
        # 4 corners of the original matrix
        A, B = (0,   0), (0,   n-1)
        D, C = (n-1, 0), (n-1, n-1)
        a,b,c,d = A,B,C,D
        
        l = n  # dimension of the square
        k = 0  # shink the square
        while l > 1:
            a, b = (A[0]+k, A[1]+k), (B[0]+k, B[1]-k) 
            d, c = (D[0]-k, D[1]+k), (C[0]-k, C[1]-k)
            for _ in range(l-1):
                self.rotate4(matrix, a,b,c,d)
                a = (a[0],   a[1]+1) 
                b = (b[0]+1, b[1])
                c = (c[0],   c[1]-1)
                d = (d[0]-1, d[1])
            k += 1
            l -= 2
        
    def rotate4(self, M, a, b, c, d):
        """a,b,c,d are tuples of (i,j) indices"""
        t = M[a[0]][a[1]]
        M[a[0]][a[1]] = M[d[0]][d[1]]
        M[d[0]][d[1]] = M[c[0]][c[1]]
        M[c[0]][c[1]] = M[b[0]][b[1]]
        M[b[0]][b[1]] = t
         
   
