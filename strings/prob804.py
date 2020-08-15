# 804 Unique Morse Code Words

# 80% solution
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        codes = dict(zip(string.ascii_lowercase,
                   [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]))

        words = set(words)

        trans = set()
        for word in words:
            tran = "".join(map(lambda c: codes[c], word))
            trans.add(tran)
        return len(trans)
