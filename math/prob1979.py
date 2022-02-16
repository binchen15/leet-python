class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        # nums.sort()
        
        # a, b = nums[0], nums[-1]
        
        a, b = sys.maxsize, 0
        
        for v in nums:
            if v < a:
                a = v
            if v > b:
                b = v
                
        for d in range(a, 0, -1):
            if a % d == 0 and b % d == 0:
                return d
      
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        # nums.sort()
        
        # a, b = nums[0], nums[-1]
        
        a, b = sys.maxsize, 0
        
        for v in nums:
            if v < a:
                a = v
            if v > b:
                b = v
                
        return math.gcd(a, b)
