# next greater element II
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        m = len(nums)
        if m == 0:
            return []
        if m == 1:
            return [-1]
        
        ans   = [-1] * m
        stack = []
        
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                d = stack[-1]
                ans[d] = n
                del stack[-1]
            stack.append(i)
        
        # wrap around. do not grow the stack this time
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                d = stack[-1]
                ans[d] = n
                del stack[-1]
            if not stack:
                break
                
        return ans 
        
