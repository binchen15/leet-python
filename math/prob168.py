class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        import string
        letters = string.ascii_uppercase
        
        n = columnNumber
        
        ans = ""
        while n > 0:
            n, r = divmod(n-1, 26)
            ans = letters[r] + ans
            
        return ans
