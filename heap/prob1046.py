class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        m = len(stones)
        if m == 0:
            return 0
        if m == 1:
            return stones[0]
       
        # python heapq module uses min heap. need flip the sign
        for i in range(m):
            stones[i] *= -1
        import heapq
        heapq.heapify(stones)
        while stones:
            if len(stones) == 1:
                return -stones[0]
            w1 = -heapq.heappop(stones)  # bigger
            w2 = -heapq.heappop(stones)  # smaller
            if w1 == w2:
                continue # both gone via pop
            else:
                heapq.heappush(stones, w2-w1)
        return 0        
        
