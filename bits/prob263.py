class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        
        while n > 1:
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else:
                return False
            
        return True
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        
        while n % 2 == 0:
            n = n // 2
        
        while n % 3 == 0:
            n = n // 3
            
        while n % 5 == 0:
            n = n // 5
            
        return n == 1
