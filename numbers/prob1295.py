class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        for n in nums:
            if self.evenDigits(n):
                cnt += 1
        return cnt
        
    def evenDigits(self, num):
        i = 1
        while num >= 10:
            num //= 10
            i += 1
        return (i & 1) == 0

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        cnt = 0
        for n in nums:
            if (int(math.log10(n)) + 1) & 1 == 0:
                cnt += 1
        return cnt

class Solution(object):
    """fastest"""
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        for n in nums:
            if len(str(n)) & 1 == 0:
                cnt += 1
        return cnt
        
