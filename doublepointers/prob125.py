class Solution(object):
    """125. Valid Palindrome. Ignore case, and consider ony alphanumeric chars"""
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = len(s)
        if m < 2:
            return True
        i = 0
        j = m - 1
        s = s.lower()
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i] == s[j]: # must both be alphanumeric 
                i += 1
                j -= 1
            else:
                return False
        return True
        
