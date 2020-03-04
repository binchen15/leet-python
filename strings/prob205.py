class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for c1, c2 in zip(s,t):
            if c1 in d:
                if d[c1] != c2:
                    return False
            else:
                if c2 in d.values(): # must be injective map
                    return False
                else:
                    d[c1] = c2
        return True
