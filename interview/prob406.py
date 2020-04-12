# 406 Queue Reconstruction by Height

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(people)
        if m <= 1:
            return people
        
        people.sort()
        ans = [0] * m
        
        for p in people:
            hgt, ind = p[0], p[1]
            j   = 0 # where to put current people
            cnt = 0 # number of taller people so far
            while cnt < ind or ans[j] != 0 :
                if ans[j] == 0:
                    cnt += 1
                else:
                    h = ans[j][0]
                    if h >= hgt:
                        cnt += 1
                j += 1
            ans[j] = p
        return ans
                    
