class Solution(object):
    """fake solution."""
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1,-1]
        
        f = nums.index(target)
        nums.reverse()
        l = len(nums) - 1 - nums.index(target)
        return [f,l]
       

class Solution(object):
		"""two O(log n) traverse"""
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        
        l, h = 0, len(nums) - 1
        while l < h:
            m = l + (h - l) // 2
            if nums[m] == target:
                h = m
            elif nums[m] < target:
                l = m + 1
            else:
                h = m - 1
        if nums[l] == target:
            ans = [l]
        else:
            return [-1, -1]
        
        l, h = 0, len(nums) - 1
        while l < h:
            m = l + (h - l + 1) // 2 # round up avoid dead loop
            if nums[m] == target:
                l = m
            elif nums[m] < target:
                l = m + 1
            else:
                h = m - 1
        ans.append(l)   # previous round guarantees that nums[l] = target
        return ans
        
             
