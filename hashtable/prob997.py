class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        from collections import defaultdict
        
        d1 = {a for a, b in trust}  # can not be judge
        
        d2 = defaultdict(int)
        for a, b in trust:
            d2[b] += 1
            
        for i in range(1, n+1):
            if i in d1:
                continue
            elif d2[i] == n-1:
                return i
            
        return -1
