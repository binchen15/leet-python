class Solution:
    def isThree(self, n: int) -> bool:
        
        if n <= 3:
            return False
        
        s = set()
        s.add(1)
        s.add(n)
        
        for i in range(2, n):
            if n % i == 0:
                s.add(i)
                if len(s) > 3:
                    return False
                
        return len(s) == 3
