# 81. Search in Rotated Sorted Array II

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        m = len(nums)
        if not m:
            return False
        if m == 1:
            return nums[0] == target
        return self.helper(nums, 0, m-1, target)
        
    def helper(self, nums, l, h, target):
        "search nums[l:h+1] for target"
        if l > h:   # cross over
            return False
        mid = l + (h-l) //2
        if nums[mid] == target:
            return True
        
        if nums[l] < nums[mid]: # sorted
            if nums[l] <= target < nums[mid]:
                return self.helper(nums, l, mid-1, target)
            else:
                return self.helper(nums, mid+1, h, target)
        elif nums[l] > nums[mid]: # right side is sorted
            if nums[mid] < target <= nums[h]:
                return self.helper(nums, mid+1, h, target)
            else:
                return self.helper(nums, l, mid-1, target)
        else: # nums[l] == nums[mid] != target # worst O(n)
            return self.helper(nums, l+1, h, target)


