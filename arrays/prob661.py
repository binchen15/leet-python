# 661 Image smoother

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """        
        nr  = len(M)
        nc  = len(M[0])
        ans = [ [0] * nc for _ in range(nr) ]
        
        for i in range(nr):
            for j in range(nc):
                nbs = [(i-1,j), (i+1,j), (i,j-1), (i,j+1), 
                       (i-1,j-1), (i+1,j+1), (i-1,j+1), (i+1,j-1),
                       (i,j)]
                avg = 0
                cnt = 0
                for x, y in nbs:
                    if 0 <= x and x < nr and \
                       0 <= y and y < nc:
                        avg += M[x][y]
                        cnt += 1
                avg  //= cnt # round down
                ans[i][j] = avg
        return ans
               

