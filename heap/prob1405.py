class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        ans = ""
        
        class Letter:
            def __init__(self, char, cnt):
                self.char = char
                self.cnt = cnt
                
            def __lt__(self, other):
                return self.cnt > other.cnt
        
        pq = []
        if a > 0:
            heapq.heappush(pq, Letter("a", a))
        if b > 0:
            heapq.heappush(pq, Letter("b", b))
        if c > 0:
            heapq.heappush(pq, Letter("c", c))

        while pq:
            lett = heapq.heappop(pq)
            if len(ans) >= 2 and ans[-2:] == lett.char * 2:
                if not pq:
                    return ans
                lett2 = heapq.heappop(pq)
                ans += lett2.char
                if lett2.cnt > 1:
                    lett2.cnt -= 1
                    heapq.heappush(pq, lett2)
                heapq.heappush(pq, lett)
            else:
                ans += lett.char
                if lett.cnt > 1:
                    lett.cnt -= 1
                    heapq.heappush(pq, lett)
        
        return ans
