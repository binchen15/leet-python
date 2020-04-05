# 49 Group Anagrams

# 10% solution
class Solution(object):
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            wc = [0] * 26  # char freq countss
            for c in s:
                wc[ ord(c) - ord('a') ] += 1
            key = ""
            for i in range(26):
                key += "{}{}".format( chr(ord('a')+i), wc[i])
            d[key] = d.get(key, []) + [s]
            
        return d.values()
