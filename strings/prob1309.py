# 1309 Decript String from Alphabet to Integer Mapping

class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = "abcdefghi"
        s2 = "jklmnopqrstuvwxyz"
        dict1 = { str(i): s1[i-1] for i in range(1,10)}
        dict2 = { str(i)+"#":s2[i-10] for i in range(10, 27)}

        m = len(s)
        i = 0 # index

        ans = ""  # to be returned
        while i < m:
            if i + 2 < m and s[i+2] == "#":
                piece = dict2[s[i:i+3]]
                i += 3
            else:
                piece = dict1[s[i]]
                i += 1
            ans += piece
        return ans

