# distinct subsequences
class Solution:

    @lru_cache(maxsize=None)
    def numDistinct(self, s: str, t: str) -> int:

        m = len(s)
        n = len(t)
        if m < n:
            return 0
        if m == n:
            return 1 if s == t else 0

        if n == 0:
            return 1

        if s[-1] != t[-1]:
            return self.numDistinct(s[:m-1], t)
        else:
            return self.numDistinct(s[:m-1], t) + self.numDistinct(s[:m-1], t[:n-1])
