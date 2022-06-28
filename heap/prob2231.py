class Solution:
    def largestInteger(self, num: int) -> int:
        
        import heapq
        
        digits = map(int, list(str(num)))
        
        parity = []
        odds = []
        evens = []
        
        for v in digits:
            if v % 2 == 1:
                heapq.heappush(odds, -v)
                parity.append(1)
            else:
                heapq.heappush(evens, -v)
                parity.append(0)
           
        ans = []
            
        for p in parity:
            if p == 1:
                ans.append(-heapq.heappop(odds))
            else:
                ans.append(-heapq.heappop(evens))
                
        return "".join(map(str, ans))
