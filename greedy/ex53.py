class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m == 1:
            return nums[0]
        if m == 0:
            return 0
        result = nums[0]
        tot    = nums[0]
        i      = 1
        while i < m:
            if tot <= 0:
                tot = nums[i]
            else: 
                tot += nums[i]
            if tot > result:
                result = tot
            i += 1
        return result
            
