
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 and isBadVersion(1):
            return 1
        
        l, h = 1, n
        while l < h:
            m = l + (h - l) // 2
            if isBadVersion(m) == True:
                h = m
            else:
                l = m + 1
        return l
                
        
