class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m <= 1:
            return m
        
        i = 0
        while i < m - 1:  # changing length
            if nums[i] == nums[i+1]:
                del nums[i+1]
                m -= 1
            else:
                i += 1
        return len(nums)
