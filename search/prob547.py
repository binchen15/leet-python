# 547 Friend circles

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M) # number of students
        if n == 0:
            return 0
        marked = [False] * n
        cnt = 0
        for i in range(n):
            if marked[i]:  # already considered
                continue
            else:
                cnt += 1
                self.friends(M, i, marked)
        return cnt
                        
    def friends(self, M, i, marked):
        # mark all friends of i, including himself
        if marked[i]:
            return 
        marked[i] = True
        for j in range(len(M)):
            if j != i and M[i][j]:
                self.friends(M, j, marked)
                
