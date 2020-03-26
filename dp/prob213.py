# 213 House Robber II. (circular neighberhood)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m == 0:
            return 0
        if m == 1:
            return nums[0]
        if m == 2:
            return max(nums)

        # 1st house is robbed. last can not be robber.
        dp1 = [0] * m  
        dp2 = [0] * m  # 1st house not robbed
        
        dp1[0] = nums[0]
        dp1[1] = nums[0]
        dp1[2] = nums[0]
        
        dp2[0] = 0
        dp2[1] = nums[1]
        dp2[2] = max(nums[1], nums[2])
        
        for i in range(3, m):
            dp1[i] = max(dp1[i-2] + nums[i-1], dp1[i-1])
            dp2[i] = max(dp2[i-2] + nums[i], dp2[i-1])
            
        return max(dp1[m-1], dp2[m-1])
            
