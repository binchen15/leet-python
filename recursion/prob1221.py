# 1221 Split string into Balanced Strings

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = len(s)
        if m == 2:
            return 1
        i = 2
        while i < m:
            if self.isBalanced(s[:i]):
                # self.balancedStringSplit(s[:i])
                return 1 + self.balancedStringSplit(s[i:])
            i += 2
        return 1

    def isBalanced(self, sub):
        return sub.count("L") == sub.count('R')
