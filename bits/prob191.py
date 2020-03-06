class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        i   = 0
        while i < 32:
            bit = n & 1
            if bit:
                cnt += 1
            n = n >> 1
            i += 1
        return cnt

class Solution(object):
    """python one liner, not fast through. B.C."""
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum(map(int, list(bin(n)[2:])))
                
