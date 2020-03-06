class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        m = len(nums)
        i = 0
        j = m-1
        while i < j:
            if nums[i] == 0:
                del nums[i]   # no need to update i
                nums.append(0)
                j -= 1
            else:
                i += 1
                
        return
