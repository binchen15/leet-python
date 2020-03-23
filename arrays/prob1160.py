# 1160 Find words can be formed by Characters

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        d = [0] * 26
        for c in chars:
            d[ ord(c) - ord('a') ] += 1
            
        ans = 0
        for word in words:
            wc = [0] * 26
            for c in word:
                i = ord(c) - ord('a')
                wc[i] += 1
            flag = True
            for i in range(26):
                if wc[i] > d[i]:
                    flag = False
                    break
            if flag:
                ans += len(word)
        return ans
        
        
