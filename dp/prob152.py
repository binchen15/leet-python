# 152
#DP 85%
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if not m:
            return 0
        if m == 1:
            return nums[0]
        
        dp_max = [0] * m
        dp_min = [0] * m
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range(1, m):
            choices = (nums[i], 
                       nums[i]*dp_min[i-1], 
                       nums[i]*dp_max[i-1])
            dp_max[i] = max(choices)
            dp_min[i] = min(choices)
            
        return max(dp_max)
        
        
                    else:
                        if v > 0:
                            dp[i] = (v*dp[i-1][0], 1 + dp[i-1][1])
                        else:
                            if i-1-
                    
            
        
