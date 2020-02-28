class Solution(object):
    """from beginning, will fail for C/C++"""
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while j < n:
            a = nums2[j]
            while i < m + j and  a > nums1[i]:
                i += 1
            nums1.insert(i, a)
            nums1.pop()
            j += 1
        return
            
            
class Solution(object):
    """from the end, should be the way to this prob"""
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 or j >= 0:
            if i < 0: # only nums2 have element not sorted
                nums1[k] = nums2[j]
                j -= 1
            elif j < 0: # only nums1 have unsorted elements
                nums1[k] = nums1[i]
                i -= 1
            elif nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        return      
