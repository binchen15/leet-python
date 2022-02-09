class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        ans = True
        
        for v in nums:
            if v == 0:
                return 0
            elif v < 0:
                ans = not ans
                
        return 1 if ans else -1 
