class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        curr = n
        while curr > 1:
            if curr % 3:
                return False
            else:
                curr = curr // 3
        return True
        
