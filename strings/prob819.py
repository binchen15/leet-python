# prob. 819 Most common word

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ban = set(banned)
        wc = self.split(paragraph.lower(), ban)
        s = sorted(wc.items(), key=lambda x: x[1], reverse=True)
        return s[0][0]

    def split(self, para, ban):
        words = {}
        i = 0
        j = 0
        m = len(para)
        while j < m:
            while j < m and para[j] not in "!?',;. ":
                j += 1
            word = para[i:j]
            if word and word not in ban:
                words[word] = words.get(word, 0) + 1
            if j == m:
                break
            else:
                j += 1
                i = j
        return words
