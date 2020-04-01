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
