# 87 Scramble String

class Solution(object):
    from collections import Counter
    
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        
        # need pruning
        if Counter(s1) != Counter(s2):
            return False
        m = len(s1)
        
        for i in range(1, m): # length of the left piece
            flag1 = self.isScramble(s1[:i], s2[:i]) and \
                    self.isScramble(s1[i:], s2[i:])
            if flag1: return True
            flag2 = self.isScramble(s1[:i],   s2[m-i:]) and \
                    self.isScramble(s1[i:], s2[:m-i])
            if flag2: return True
        return False   
        

