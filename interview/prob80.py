# 80 Remove Duplicats from sorted array II

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m <= 2:  # nothing to do
            return m
        
        i = 0
        while i < m: # length changes 
            if i+1 == m or nums[i+1] != nums[i]:
                i += 1
            else:
                if i+2 == m or nums[i+2] != nums[i]:
                    i += 1
                else:
                    del nums[i]
					# m -= 1  fine too
            m = len(nums)              
        return len(nums)


