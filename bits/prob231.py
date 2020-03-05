class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        foundOne = False
        while n > 0:
            bit = n & 1  # last bit
            if bit:
                #print("here")
                if foundOne:
                    return False
                else:
                    foundOne = True
            n = n >> 1
        return foundOne
