# 377 Combination Sum IV (Medium)

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < 0:
            return 0
        if target == 0:
            return 1
        
        m  = len(nums)
        dp = [0] * (target+1)
        dp[0] = 1
        nums.sort()
        
        for t in range(1, target+1):
            for i in range(m):
                v = nums[i]
                if v <= t:
                    dp[t] += dp[t-v] # append a number v
                else:
                    break
        return dp[target]
                    
