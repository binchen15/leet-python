class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
            
        return len(set(d.values())) == 1
