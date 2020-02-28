class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = len(s)
        i = 0
        j = m - 1
        token = 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif token == 0: # already used
                return False
            else:
                token = 0    # which route is right? buggy here..
                if s[i] == s[j-1]:
                    j -= 1
                elif s[i+1] == s[j]:
                    i += 1
                else:
                    return False
        return True        
        
                
class Solution(object):
    """this fails with memory limit error when submitting"""
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.validPalindrome_with_token(s, True)
    
    def validPalindrome_with_token(self, s, token):
        #print(s)
        if len(s) <= 1:
            return True
        if len(s) == 2:
            if token:
                return True
            elif s[0] == s[1]:
                return True
            else:
                return False
        if s[0] == s[-1]:
            return self.validPalindrome_with_token(s[1:-1], token)
        else:
            if token:
                return self.validPalindrome_with_token(s[:-1], False) or self.validPalindrome_with_token(s[1:], False)
            else:
                return False
            
        
class Solution(object):
    """first success version"""

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = len(s)
        i = 0
        j = m - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.valid(s[i+1:j+1]) or self.valid(s[i:j])
        return True
       
    def valid(self, s):
        m = len(s)
        i = 0
        j = m - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
