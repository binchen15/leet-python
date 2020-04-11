# 238 Product of Array Except Self

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = len(nums)
        dp1 = [0] * m
        dp2 = [0] * m

        dp1[0] = nums[0]
        for i in range(1, m):
            dp1[i] = dp1[i-1]*nums[i]
        dp2[m-1] = nums[m-1]
        for i in range(m-2, -1, -1):
            dp2[i] = dp2[i+1]*nums[i]
            
        output = [0] * m
        output[0]   = dp2[1]
        output[m-1] = dp1[m-2]
        for i in range(1, m-1):
            output[i] = dp1[i-1]*dp2[i+1]              
        return output
        
