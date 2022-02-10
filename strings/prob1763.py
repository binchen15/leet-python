class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        ans = ""
        n = len(s)
        
        for i in range(n-1):
            for j in range(i+1, n):
                tmp = s[i:j+1]
                if self.isNice(tmp) and len(tmp) > len(ans):
                    ans = tmp
        return ans
        
        
    def isNice(self, s):
        s = set(s)
        for c in s:
            if c.islower() and chr(ord(c) - 32) not in s:
                return False
            if c.isupper() and chr(ord(c) + 32) not in s:
                return False
        return True
