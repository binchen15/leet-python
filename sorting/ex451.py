# sort characters by Frequency

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        f = {}
        for c in s:
            f[c] = f.get(c, 0) + 1
        f_sorted = sorted(f.items(), key = lambda x: x[1], reverse =True)
        strs = [ p[0] * p[1] for p in f_sorted ]
        return "".join(strs)
