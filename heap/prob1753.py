class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        
        class Stone:
            def __init__(self, v):
                self.val = v
                
            def __lt__(self, other):
                return self.val > other.val
            
            
        pq = [Stone(a), Stone(b), Stone(c)]
        heapq.heapify(pq)
        
        score = 0
        
        while len(pq) >= 2:
            s1, s2 = heapq.heappop(pq), heapq.heappop(pq)
            score += 1
            s1.val -= 1
            s2.val -= 1
            
            if s1.val > 0:
                heapq.heappush(pq, s1)
            if s2.val > 0:
                heapq.heappush(pq, s2)
                
        return score
