# 387 first unique character in a string

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        f = {}
        for c in s:
            f[c] = f.get(c, 0) + 1
        u = filter(lambda x : x[1] == 1, f.items())
        k = map(lambda x : x[0], u)
        if not k:
            return -1
        for i, c in enumerate(s):
            if c in k:
                return i
        return -1

# O(n)
class Solution(object):
    
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        f = {}
        for i, c in enumerate(s):
            if c in f:
                f[c] = -1
            else:
                f[c] = i
        pairs = sorted(filter(lambda x : x[1] != -1, f.items()), 
                        key = lambda x: x[1])
        if pairs:
            return pairs[0][1]
        else:
            return -1 
        
            
        
