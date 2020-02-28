# longest word in the dictironary with smallest lexicographic order
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        record = 0
        ans    = ""
        for word in d:
            if self.isParent(s, word):
                if len(word) > record or \
                   (len(word) == record and word <= ans):
                    record = len(word)
                    ans   = word
        return ans
            
        
    def isParent(self, s, word):
        """is s parent of word"""
        ms = len(s)
        mw = len(word)
        i = 0
        j = 0
        while i < ms and j < mw:
            if s[i] == word[j]:
                i += 1
                j += 1
            else:
                i += 1
        if j == mw:
            return True
        else:
            return False
                
        
