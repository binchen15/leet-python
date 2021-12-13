class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        n = len(s)
        if n == 1:
            return [1]
        
        def findLastIndex(c):
            """find last occurrence/index of char c assuming c exists"""
            try:
                return s.rindex(c)
            except:
                return -1
        
        import string
        d = {c: findLastIndex(c) for c in string.ascii_lowercase}
        
        ans = []
        l = 0 # left boundary of current partition
        while l < n:
            r = d[s[l]] # tentative right boundary of current partition
            if l == r or l == r-1:
                ans.append(r-l+1)
                l = r+1
            else:   
                cur = l+1
                while cur < r:
                    tmp = d[s[cur]]
                    r = max(r, tmp)  # extend right boundary for char in the middle if needed
                    cur += 1
                ans.append(r-l+1)
                l = r+1
        return ans

