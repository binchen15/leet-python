#Scramble string
# recursion =+ memoization
class Solution:

    @lru_cache(maxsize=None)
    def isScramble(self, s1: str, s2: str) -> bool:

        n = len(s1)

        if n == 1:
            return s1 == s2

        if n == 2:
            return s1 == s2 or s1 == s2[::-1]

        for i in range(1, n):
            if self.isScramble(s1[:i], s2[:i]) and \
                self.isScramble(s1[i:], s2[i:]):
                return True

            if self.isScramble(s1[:i], s2[n-i:]) and \
                self.isScramble(s1[i:], s2[:n-i]):
                return True
