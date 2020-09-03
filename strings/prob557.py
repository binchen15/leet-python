# 557 Reverse Words in a string III

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        rev_words = map(self.reverse, words)
        return " ".join(rev_words)

    def reverse(self, word):
        a = list(word)
        a.reverse()
        return "".join(a)
