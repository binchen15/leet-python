# 3 longest substring without repeating characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        if n <= 1:
            return n

        d = set()
        res = 1

        r = 0
        for l in range(n):
            while r < n and s[r] not in d:
                d.add(s[r])
                res = max(res, r-l+1)
                r += 1
            d.remove(s[l])
        return res
