class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counts = {0:0, 1:0, 2:0}
        for num in nums:
            counts[num] += 1
        for i in range(counts[0]):
            nums[i] = 0
        for i in range(counts[0],counts[0]+counts[1]):
            nums[i] = 1
        for i in range(counts[0]+counts[1],counts[0]+counts[1]+counts[2]):
            nums[i] = 2
        return

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        m     = len(nums)
        start = 0
        end   = m - 1
        i     = 0
        while start <= end and i <= end:
            a = nums[i]
            if a == 2:
                self.swap(nums, i, end)
                end -= 1
				# i += 1 no! i might have 0, or 1 need while again
            elif a == 0:
                self.swap(nums, i, start)
                start += 1 
                i += 1
            else:
                i += 1
                              
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
                
                        
