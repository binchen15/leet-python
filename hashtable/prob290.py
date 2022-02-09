class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split(" ")
        n = len(words)
        if n != len(pattern):
            return False
        
        m = {}  # store the bijection
        for i, c in enumerate(pattern):
            if c not in m:
                m[c] = words[i]
            else:
                if m[c] != words[i]:
                    # print(m)
                    return False
        
        return len(m) == len(set(m.values()))

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split(" ")
        n = len(words)
        if n != len(pattern):
            return False
        
        m = {}  # map
        r = {}  # reverse map
        for i, c in enumerate(pattern):
            w = words[i]
            if c not in m:
                if w in r:
                    return False
                else:
                    m[c] = w
                    r[w] = c
            else:
                if m[c] != w:
                    return False
        
        return True

