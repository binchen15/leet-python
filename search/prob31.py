class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        
        def findUB(i):
            """find the lowest upper bound of nums[i-1] from nums[i:]"""
            v = nums[i-1]
            curr = i
            while curr+1< n and nums[curr+1] > v:
                curr += 1
            return curr
                
                
        def reverse(i):
            """reverse nums[i:]"""
            l = n-i
            h = l // 2
            for k in range(h):
                nums[i+k], nums[n-1-k] = nums[n-1-k], nums[i+k]
        
        # find i such as nums[i-1] < nums[i] and nums[i:] is decreasing
        i = n-1
        while i-1>=0 and nums[i-1] >= nums[i]:
            i -= 1
        if i-1 >= 0:
            j = findUB(i)
            nums[i-1], nums[j] = nums[j], nums[i-1]
            reverse(i)
        else:
            reverse(0)

