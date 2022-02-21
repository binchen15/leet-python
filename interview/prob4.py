# Median of two sorted array

# binary method
# merge(nums1[:m], nums2[:n]) to the first half.
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # forces nums1 to be the shorter one
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        l1 = len(nums1)
        l2 = len(nums2)
        k  = (l1 + l2) // 2 # desired length of the first half
        
        l, h = 0, l1
        while l < h:
            m = l + (h-l)//2
            n = k - m
            if nums1[m] < nums2[n-1]:
                l = m + 1
            else:
                h = m
        
        m = l
        n = k - m
        c1 = max( nums1[m-1] if m > 0 else -float('inf'),
                  nums2[n-1] if n > 0 else -float('inf'))
        
        c2 = min( nums1[m] if m < l1 else float('inf'),
                  nums2[n] if n < l2 else float('inf'))
        
        if (l1 + l2) & 1:
            return c2
        else:
            return 0.5*(c1+c2)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m = len(nums1)
        n = len(nums2)
        
        if m == 0:
            return self.helper(nums2)
        if n == 0:
            return self.helper(nums1)
        
        nums = self.merge(nums1, nums2)
        
        return self.helper(nums)
        
    def helper(self, nums):
        n = len(nums)
        if n % 2 == 0:
            return 0.5*( nums[n//2] + nums[n//2-1])
        else:
            return nums[n // 2]
        
    def merge(self, nums1, nums2):
        
        m = len(nums1)
        n = len(nums2)
        nums = []
        p1, p2 = 0, 0
        
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                nums.append(nums1[p1])
                p1 += 1
            else:
                nums.append(nums2[p2])
                p2 += 1
                
        if p1 != m:
            nums.extend(nums1[p1:m])
        if p2 != n:
            nums.extend(nums2[p2:n])
                
        return nums
