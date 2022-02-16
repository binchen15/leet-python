class Solution:
    def sumBase(self, n: int, k: int) -> int:
        
        ans = 0
        
        while n > 0:
            n, r = divmod(n, k)
            ans += r
            
        return ans
