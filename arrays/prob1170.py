# 1170 Compare strings by frequency of smallest character

# 50% solution
class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        fc = [ self.f(word) for word in words]
        fc.sort(reverse=True)
        
        ans = []
        for q in queries:
            c = self.f(q)
            ans.append(self.compare(c, fc))
        return ans
        
    def f(self, word):
        wc = {}
        for c in word:
            wc[c] = wc.get(c, 0) + 1
        return sorted(wc.items(), key=lambda x : x[0])[0][1]
    
    def compare(self, c, fc):
        """fc is sorted, non-decreasing"""
        cnt = 0
        for n in fc:
            if c < n:
                cnt += 1
            else:
                break
        return cnt
        
