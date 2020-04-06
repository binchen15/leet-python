# 151. Reverse Words in a String

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #s = s.strip()
        words = s.split() # will auto-drop empty word
        words.reverse()
        return " ".join(words)
        
        
