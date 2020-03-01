class Solution(object):
		"""ugly... not feeling well today"""
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)
        i = 0
        j = 0
        while j < n and i < m:
            if s[i] == t[j]:
                j += 1
                i +=1
            else:
                j += 1
        if j == n:
            if i < m:
                return False
            else:
                return True
        else:
            return True

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)
        i = 0
        j = 0
        if m == 0:
            return True
        while j < n:
            if s[i] == t[j]:
                j += 1
                i += 1
                if i == m:
                    return True
            else:
                j += 1
        return False

