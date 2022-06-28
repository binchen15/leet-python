class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        for i in range(len(piles)):
            piles[i] *= -1
            
        heapq.heapify(piles)  # max heap now
        
        for i in range(k):
            if -piles[0] == 1:
                break 
            v = -heapq.heappop(piles)
            heapq.heappush(piles, -(v - v // 2) )
                
        return -sum(piles)
