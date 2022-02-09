class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        
        target = min(nums)
        ans = self.helper(target)
        
        return 0 if ans % 2 == 1 else 1
        
    def helper(self, num):
        
        ans = 0
        while num > 0:
            num, mod = divmod(num, 10)
            ans += mod
            
        return ans
