# 703 Kth Largest Element in a Stream

# this fails with time limit error
class KthLargest(object):
    import heapq
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.nums, val)
        # this is too slow
        return heapq.nlargest(self.k, self.nums)[-1]

class KthLargest(object):
    import heapq
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.min_heap = []
        for i, n in enumerate(nums):
            if i < k:
                heapq.heappush(self.min_heap, n)
            else:
                if n > self.min_heap[0]:
                    heapq.heapreplace(self.min_heap, n)
                
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)
        return self.min_heap[0]
        
