class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        
        counters = {}
        for v in position:
            counters[v] = counters.get(v, 0) + 1
            
        ans = sys.maxsize
        
        for p in counters:
            cost = 0
            for q in counters:
                if q != p:
                    if abs(q-p) % 2:
                        cost +=  counters[q]
            if cost < ans:
                ans = cost
                
        return ans
