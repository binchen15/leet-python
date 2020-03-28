# 376 Wiggle Subsequence

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m <= 1:
            return m
        
		# wiggling seq ends at i, with is going up/down at the last step
        dp1 = [1] * m  # up
        dp2 = [1] * m  # down
        
        for i in range(1, m):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp1[i] = max(dp1[i], dp2[j]+1)
                elif nums[i] < nums[j]:
                    dp2[i] = max(dp2[i], dp1[j]+1)
        l1 = max(dp1)
        l2 = max(dp2)
        return max(l1, l2)
