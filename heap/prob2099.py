class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        class Number:
            def __init__(self, i, v):
                self.i = i
                self.val = v
                
            def __lt__(self, other):
                return self.val > other.val
        
        pq = []
        
        for i, v in enumerate(nums):
            heapq.heappush(pq, Number(i, v))
            
        tmp = [ heapq.heappop(pq) for i in range(k)]
        
        tmp.sort(key = lambda x: x.i)
        
        ans =  [ number.val for number in tmp ]
        
        return ans
