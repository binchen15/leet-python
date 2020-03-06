class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        r0 = len(nums)
        if r0:
            c0 = len(nums[0])
        else:
            c0 = 0
        if not r0*c0 or r0*c0 != r*c:
            return nums
        
        #### this array initialization make shallow copy.. 
        #### subtle error. wasted 2 hours on it.
        row = [0] * c
        ans = [row] * r
        
        for i in range(r):
            for j in range(c):
                k = i * c + j
                i0 = k // c0
                j0 = k  % c0
                ans[i][j] = nums[i0][j0]
        return ans

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        r0 = len(nums)
        if r0:
            c0 = len(nums[0])
        else:
            c0 = 0
            
        if not r0*c0 or r0*c0 != r*c:
            return nums
        
        ans = [ [0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                k = i * c + j
                i0 = k // c0
                j0 = k  % c0
                ans[i][j] = nums[i0][j0]
        return ans
        
        
