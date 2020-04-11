# 581 Shorted Unsorted Continuoous Subarray

# two pointers 90% solution 
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m <= 1: # weird though
            return 0
        asec = sorted(nums) # sorted 
        i, j = 0, m-1
        while i < m and nums[i] == asec[i]:
            i += 1
        if i == m: # already sorted
            return 0
        
        while j >= 0 and nums[j] == asec[j]:
            j -= 1
        return j - i + 1
            
