# 198 House Robber

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if not m:
            return 0
        if m == 1:
            return nums[0]
        if m == 2:
            return max(nums[0], nums[1])
        
        dp    = [0] * m
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, m):
            """two scenarios, did I rob the last one or not"""
            dp[i] = max(dp[i-2] + nums[i],  # yes 
						dp[i-1])            # no
            
        return dp[m-1]
        
