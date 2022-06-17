class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        
        nums.sort(reverse=True)
        
        tot = sum(nums)
        
        i = 0
        ps = nums[0] # partial sum
        while ps <= tot - ps:
            i += 1
            ps += nums[i]
            
        return nums[:i+1]
