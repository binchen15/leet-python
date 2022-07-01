class Solution:
    def numSplits(self, s: str) -> int:
        
        n = len(s)
        if n <= 1:
            return 0
        
        l, r = {}, {}
        for c in s:
            r[c] = r.get(c, 0) + 1
            
        ans = 0
        for c in s:
            l[c] = l.get(c, 0) + 1
            r[c] = r[c] - 1
            if r[c] == 0:
                del r[c]
            if len(l) == len(r):
                ans += 1
                
        return ans
