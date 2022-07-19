#Prob.76 Minimum Window Substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        n = len(s)
        d = collections.Counter(t)
        m = len(d)  # number of unique keys

        formed = 0  # for how many keys we have zero balance

        ans = ""
        min_len = sys.maxsize

        l = 0
        for r in range(n):  # s[l:r+1]
            ch = s[r]
            if ch not in d:
                continue
            d[ch] -= 1  # found one char
            if d[ch] == 0:
                formed += 1

            while l <= r and formed == m:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    ans = s[l:r+1]
                c = s[l]
                l += 1
                if c not in d:
                    continue
                else:  # lose one good char by move l to the right
                    d[c] += 1
                    if d[c] == 1:
                        formed -= 1

        return ans

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        m, n = len(s), len(t)
        if m < n:
            return ""
        
        cnts = {}
        for c in t:
            cnts[c] = cnts.get(c, 0) + 1
            
        ans = ""
        size = sys.maxsize
            
        valid = 0  # how many valid chars we found 
        l = 0      # move fast
        for r in range(m): # move slow
            c = s[r]
            if c in cnts:
                cnts[c] -= 1
                if cnts[c] == 0:
                    valid += 1
                
                if valid == len(cnts): # this is a valid window
                    # update the result
                
                    while s[l] not in cnts or cnts[s[l]] < 0: # still have balance remained
                        if s[l] in cnts:
                            cnts[s[l]] += 1
                        l += 1
                    if r-l+1 < size:
                        size = r-l+1
                        ans = s[l:r+1]
                    
                            
        return ans

