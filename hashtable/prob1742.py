class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        
        def sumDigits(n):
            
            s = 0
            while n > 0:
                n, r = divmod(n, 10)
                s += r
                
            return s
                
        d = {}
        for i in range(lowLimit, highLimit+1):
            s = sumDigits(i)
            d[s] = d.get(s, 0) + 1
            
        return max(d.values())
