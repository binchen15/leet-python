# 367 Valid  Perfect Square

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return 1

        l, h = 1, num

        while l <= h:
            m = (l + h) // 2
            m2 = m * m
            if m2 == num:
                return True
            elif m2 < num:
                l = m + 1
            else:
                h = m - 1

        return False
