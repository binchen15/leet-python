class Solution(object):
    """brutal force method. 45%"""
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m == 1:
            return nums[0]
        i = 0
        while i < m - 1:
            if nums[i] != nums[i+1]:
                return nums[i]
            else:
                i += 2
        return nums[m - 1]

class Solution(object):
    """uggly solution."""
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        
        l, h = 0, m-1
        while True:
            mid = l + (h - l) // 2
            if mid == 0:
                return nums[1]
            if mid == m-1:
                return nums[-2]  
            if nums[mid] != nums[mid+1] and \
               nums[mid] != nums[mid-1]:
                return nums[mid]
            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    l = mid + 2
                else:
                    h = mid - 2
            else:  # odd
                if nums[mid] == nums[mid-1]:
                    l = mid + 2
                else:
                    h = mid - 1

            
