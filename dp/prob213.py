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

# DP solution. 
class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n <= 3:
            return max(nums)

        def helper(i, j):
            """nums[i, j+1]"""
            if j-i < 2:
                return max(nums[i:j+1])

            dp = [0] * (j-i+1)
            dp[0] = nums[i]
            dp[1] = max(nums[i], nums[i+1])
            for k in range(2, j-i+1):
                dp[k] = max(dp[k-1], nums[i+k]+dp[k-2])

            #print(dp)
            return dp[j-i]

        p1 = helper(1, n-1) # not robbing first house
        p2 = nums[0] + helper(2, n-2)
        #print(p1, p2)

        return max(p1, p2)
