class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        
        n = len(nums)
        l, r = 0, n-1
        
        ans = nums[l] + nums[r]
        
        while l < r:
            tmp = nums[l] + nums[r]
            ans = max(ans, tmp)
            
            l += 1
            r -= 1
            
        return ans
