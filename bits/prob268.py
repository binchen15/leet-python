class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ans = 0
        for i, n in enumerate(nums):
            ans = ans ^ n ^ i
        ans ^= len(nums)
        return ans
        
