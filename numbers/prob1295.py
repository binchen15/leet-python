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
        
