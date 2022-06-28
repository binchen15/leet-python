class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        cnts = {i: 0 for i in range(n)}
        
        for a, b in roads:
            cnts[a] += 1
            cnts[b] += 1
            
        duals = zip([i for i in range(n, 0, -1)], sorted(cnts.values(), reverse=True))
        
        tot = 0
        for v, c in duals:
            tot += v * c
            
        return tot
