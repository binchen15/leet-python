# 55 Jump Game

# 5% solution O(n^2)
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = len(nums)
        if m <= 1:
            return True
        
        dp = [False] * m
        dp[0] = True
        for i in range(1, m):
            for j in range(i-1, -1, -1):
                if dp[j] and nums[j] >= (i-j):
                    dp[i] = True
                    break
        return dp[m-1]


