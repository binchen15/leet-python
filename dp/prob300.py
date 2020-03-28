# 300 Longest Increasing Subsequence

#comment: how to define dp[i] is critical
# it is not the LIS result for nums[:i+1]

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m <= 1:
            return m
        # dp[i] length of LIS "which ends at nums[i]"
        dp = [1] * m
        for i in range(1, m):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)   
