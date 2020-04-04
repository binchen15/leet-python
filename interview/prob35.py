# 35 Search Insert Position

# binary search.
# return l, not r if not found since they cross over
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        m = len(nums)
        if not m:
            return 0
        if target < nums[0]:
            return 0
        if target > nums[m-1]:
            return m
        
        l, r = 0, m-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l += 1
            else:
                r -= 1
        return l
        
