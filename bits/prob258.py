class Solution:
    def addDigits(self, num: int) -> int:
        
        if num < 10:
            return num
        
        nxt = 0
        while num > 0:
            num, mod = num // 10, num % 10
            nxt += mod
            
        return self.addDigits(nxt)
