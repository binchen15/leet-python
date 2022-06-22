# 392 Is Subsequence

# two pointers 90% solution

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)

        i = 0 # pointer in s
        j = 0 # pointer in t

        while i < m:
            while j < n and t[j] != s[i]:
                j += 1
            if j == n:
                return False
            else:
                i += 1
                j += 1
        return True

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        m = len(s)
        n = len(t)

        if m > n:
            return False

        i, j = 0, 0

        while i < m: # match s[i]
            while t[j] != s[i] and j+1 < n:
                j += 1

            if t[j] == s[i]:
                i += 1
                j += 1
                if i < m and j == n:
                    return False
            else:
                return False

        return True
