class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        sgn = 1
        
        for v in nums:
            if v == 0:
                return 0
            elif v < 0:
                sgn *= -1
                
        return sgn

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        count = 0
        
        for v in nums:
            if v == 0:
                return 0
            elif v < 0:
                count += 1
                
        return -1 if count % 2 == 1 else 1
