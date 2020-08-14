# 520 Detect Captical

# is word in correct Capital case?

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1 or word.isupper() or word.islower():
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        return False
