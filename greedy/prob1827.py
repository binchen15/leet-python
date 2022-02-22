class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        ans = 0
        if n <= 1:
            return ans
        
        cur = nums[0]
        for i in range(1, n):
            if nums[i] <= cur:
                tmp = cur - nums[i] + 1
                ans += tmp
                cur = cur + 1
            else:
                cur = nums[i]
                
        return ans
