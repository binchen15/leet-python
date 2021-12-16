class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        d = dict(zip(string.ascii_uppercase, range(1,27)))
            
        ans = 0
        for c in columnTitle:
            ans = ans*26 + d[c]
        return ans

