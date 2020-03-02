class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        l, h = 1, x # lower/upper bound for bisec
        while l <= h:
            mid = l + (h - l) // 2 # want integer
            if mid * mid == x:
                return mid
            elif mid * mid < x :
                l = mid + 1
            else:
                h = mid - 1
        return h    # h = l-1 when quit the while loop
        
