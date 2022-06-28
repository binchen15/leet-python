class Solution:
    def frequencySort(self, s: str) -> str:
        
        cnts = {}
        
        for c in s:
            cnts[c] = cnts.get(c, 0) + 1
            
        pairs = sorted(cnts.items(), key = lambda x: x[1], reverse=True)
        
        ans = ""
        for char, cnt in pairs:
            ans += char * cnt
            
        return ans
