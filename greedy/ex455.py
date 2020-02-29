class Solution(object):
    """prob455 assign cookie"""
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                j += 1 # next cookie
                i += 1 # next boy
            else:
                j += 1 # next cookie
        return i
        
