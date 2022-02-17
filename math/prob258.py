class Solution:
    def addDigits(self, num: int) -> int:
        
        def helper(n):
            s = 0
            while n > 0:
                n, r = divmod(n, 10)
                s += r
            return s
        
        while num >= 10:
            num = helper(num)
            
        return num
