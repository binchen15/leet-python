# is a number palindrome

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        word = str(x)
        m = len(word)
        if m <= 1:
            return True
        
        for i in range(m // 2):
            if word[i] != word[m-1-i]:
                return False
        return True
        

