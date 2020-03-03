class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        if L == 1:
            return nums[0]
        if nums[0] < nums[-1]:  # un-rotated case
            return nums[0]

        # goal: reduce the distance from l to  to 1.
        l, h = 0, L-1
        while l < h:
            if l + 1 == h:
                return nums[h]
            m = l + (h-l) // 2  # l < m < h
            if nums[l] > nums[m]:
                h = m
            else:
                l = m
