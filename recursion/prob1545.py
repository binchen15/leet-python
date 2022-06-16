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
