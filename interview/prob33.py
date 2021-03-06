# 33 Search in Rotated Sorted Array

# 30% in speed
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        m = len(nums)
        if not m:
            return -1
        if m == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
            
        if nums[0] < nums[m-1]: # not rotated
            return self.binarySearch(nums, target)
            
        # FIND THE PIVOT POSITION (L,H)
        l, h = 0, m - 1
        while l < h-1:
            mid = l + (h-l)//2
            if nums[mid] >= nums[l]:
                l = mid
            else:
                h = mid
        # l+1 = h
        if target > nums[l] or target < nums[h]:
            return -1
        if target <= nums[-1]:
            ind = self.binarySearch(nums[h:], target)
            return ind if ind == -1 else ind + h
        else:
            return self.binarySearch(nums[:h], target)
             
    def binarySearch(self, nums, target):
        m = len(nums)
        l, h = 0, m-1
        while l <= h:
            mid = l + (h-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                h = mid - 1
            else:
                l = mid + 1
        return -1
        
# 97% solution
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        m = len(nums)
        if not m:
            return -1
        return self.searchBinary(nums, 0, m-1, target)
        
        
    def searchBinary(self, nums, l, h, target):
        """search nums[l:h+1] for target"""
        if l > h:
            return -1
        mid = l + (h-l)//2
        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]: # left side sorted
            if nums[l] <= target <= nums[mid]:
                return self.searchBinary(nums, l, mid, target)
            else:
                return self.searchBinary(nums, mid+1, h, target)
        else:   # right side is sorted
            if nums[mid] <= target <= nums[h]:
                return self.searchBinary(nums, mid, h, target)
            else:
                return self.searchBinary(nums, l, mid-1, target)
        
                  
