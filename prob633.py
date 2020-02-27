class Solution(object):
    """square sum """
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        #l = range(c+1)
        import math
        i = 0
        j = math.floor(math.sqrt(c))
        while i*i + j*j != c:
            if i*i + j*j > c:
                j -= 1
            else:
                i += 1
            if j < i:
                return False
        return True


