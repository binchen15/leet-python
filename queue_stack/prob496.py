class Solution(object):
    """46%"""
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m = len(nums1)
        n = len(nums2)
        if m == 0:
            return []
        if n == 1:
            return [-1]
        
        ans = [-1] * m
        
        tgt = set(nums1)
        stack = []
        for v in nums2:
            while stack and nums1[stack[-1]] < v:
                d = stack[-1]
                ans[d] = v
                del stack[-1]
            if v in tgt:
                stack.append(nums1.index(v))
                
        return ans
                
class Solution(object):
    """80% performance """
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m = len(nums1)
        n = len(nums2)
        if m == 0:
            return []
        if n == 1:
            return [-1]
        
        ans = [-1] * m
        
        tgt = {v : i for i, v in enumerate(nums1) }
        stack = []
        for v in nums2:
            while stack and nums1[stack[-1]] < v:
                d = stack[-1]
                ans[d] = v
                del stack[-1]
            if v in tgt:
                stack.append(tgt[v])
                
        return ans
                
                

