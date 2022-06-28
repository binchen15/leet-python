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

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        import heapq

        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) >= 2:
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)
            if s1 != s2:
                heapq.heappush(stones, s1-s2)

        if len(stones) == 1:
            return -stones[0]
        return 0

