class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        digits = self.convert(s)
        
        for i in range(k):
            digits = self.transform(digits)
            if len(digits) == 1:
                break
            
        return int(digits)
        
    def convert(self, s: str) -> str:
        
        offset = ord('a') - 1
        l = [ str(ord(c) - offset) for c in s]
        
        return "".join(l)
        
    def transform(self, s: str) -> str:
    
        ans = 0
        for d in s:
            ans += int(d)
            
        return str(ans)
