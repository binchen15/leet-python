# 1545 Find Kth Bit in Nth Binary string

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        s = self.sn(n)
        
        return s[k-1]
        
    
    def sn(self, n):
        if n == 1:
            return "0"
        
        p = self.sn(n-1)
        return p + "1" + self.reverse(self.invert(p))
                
    def invert(self, s):
        return "".join(map(lambda c : str(int(c) ^ 1), s))
        
    def reverse(self, s):
        return s[::-1]

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        s = "0"
        for i in range(1, n):
            s = s + "1" + self.invert(s)
        return s[k-1]
        
    def invert(self, s):
        m = {"1":"0", "0":"1"}
        return "".join([m[c] for c in s])[::-1]

