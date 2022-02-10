class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        n = columnNumber
        ans = ""
        
        while n > 0:
            n, r = divmod(n-1, 26)
            char = chr(ord("A") + r)
            ans = char + ans
            
        return ans
