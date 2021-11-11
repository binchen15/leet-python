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
