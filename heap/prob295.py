import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.size = 0

    def addNum(self, num: int) -> None:
        
        if self.size == 0:
            self.max_heap.append(-num)
        else:
            val = -self.max_heap[0]
            if num <= val:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
            
        self.size += 1
        
        self.rebalance()
        
    def rebalance(self):
        l = len(self.max_heap)
        r = len(self.min_heap)
        while l < r-1:
            v = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -v)
            r -= 1
            l += 1
            
        while l > r + 1:
            v = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -v)
            l -= 1
            r += 1
             

    def findMedian(self) -> float:
        
        l = len(self.max_heap)
        r = len(self.min_heap)
        
        if l == r:
            v1 = -self.max_heap[0]
            v2 = self.min_heap[0]
            return 0.5*(v1+v2)
        elif l == r - 1:
            return self.min_heap[0]
        else:
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
