# 312 Burst Ballons

# not working....

# Brute Force. TLE
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not n:
            return 0
        if n == 1:
            return nums[0]
        
        ans = [0]
        self.helper(nums, 0, ans)
        return ans[0]
        
    def helper(self, nums, curr, ans):
        if not nums:
            if curr > ans[0]:
                ans[0] = curr
            return        
        m = len(nums)
        if m == 1:
            tot = curr + nums[0]
            if tot > ans[0]:
                ans[0] = tot
            return
        if m == 2:
            tot = curr + nums[0]*nums[1] + max(nums[0], nums[1])
            if tot > ans[0]:
                ans[0] = tot
            return
        self.helper(nums[1:],   curr+nums[0]*nums[1], ans)
        self.helper(nums[:m-1], curr+nums[-2]*nums[-1], ans)
        for i in range(1, m-1):
            self.helper(nums[:i]+nums[i+1:], curr+nums[i-1]*nums[i]*nums[i+1], ans)
            

