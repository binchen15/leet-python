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

