# 30 Substring with Concatenation of All Words

# 40% solution.
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        m = len(s)
        if not m or not words:
            return []
        
        wc = {}
        for w in words:
            wc[w] = wc.get(w, 0) + 1
            
        nw = len(words)     # number of words
        wl = len(words[0])  # word length
        l  = nw * wl # length of substr to test
        
        ans = []
        if m < l:
            return ans
        for i in range(m-l+1):
            if self.verify(nw, wl, s,i, wc):
                ans.append(i)
        return ans
    
    def verify(self, nw, wl, s, i, wc):
        j = i
        d = {}
        for k in range(nw):
            w = s[j:j+wl]
            if w not in wc:
                return False
            else:
                d[w] = d.get(w, 0) + 1
                j   += wl
        return d == wc
            
        
