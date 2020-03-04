class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1 = [0] * 26
        l2 = [0] * 26
        
        offset = ord('a')
        for c in s:    
            l1[ord(c)-offset] += 1
        for c in t:
            l2[ord(c)-offset] += 1
        return l1 == l2
        
