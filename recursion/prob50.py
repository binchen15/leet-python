class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n < 0:
            return 1.0/self.myPow(x, -n)
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n == 2:
            return x*x
        
        q, r = n // 2, n % 2
        t = self.myPow(x, q)
        return t*t*self.myPow(x, r)

class Solution:
    def myPow(self, x: float, n: int) -> float:
      
        memo = {}
    
        @lru_cache(None)
        def helper(n):
            if n < 0:
                return 1.0/helper(-n)
            if n == 0:
                return 1.0
            if n == 1:
                return x
            if n == 2:
                return x*x
            
            
            q, r = n // 2, n % 2
            t = helper(q)
            ans = t*t*helper(r)
            return ans
        
        return helper(n)

# log(n)
class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(n):
            if n < 0:
                return 1.0/helper(-n)
            if n == 0:
                return 1.0
            if n == 1:
                return x
            if n == 2:
                return x*x

            q, r = n // 2, n % 2
            t = helper(q)
            ans = t*t
            if r == 1:
                ans *= x
            return ans

        return helper(n)

