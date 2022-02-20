class Solution:
    def minOperations(self, n: int) -> int:
        
        if n == 1:
            return 0
        
        l, r = 0, n-1
        ops = 0
        
        while l < r:
            a, b = 2*l+1, 2*r+1
            ops += (b-a) // 2

            l += 1
            r -= 1
        
        return ops

class Solution:
    def minOperations(self, n: int) -> int:

        if n == 1:
            return 0

        l, r = 0, n-1
        a, b = 2*l+1, 2*r+1
        dops = (b-a) // 2

        ops = 0

        while dops > 0:
            ops += dops
            dops -= 2
        return ops

class Solution:
    def minOperations(self, n: int) -> int:
        
        if n == 1:
            return 0
        
        l, r = 0, n-1
        a, b = 2*l+1, 2*r+1
        dops = r - l 
        
        if dops % 2 == 0:
            m = dops // 2
            ans = m * (2 + dops) // 2
        else:
            m = (dops + 1) // 2
            ans = m * (1 + dops) // 2
            
        return ans
