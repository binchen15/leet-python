class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return nums[k-1]

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        h = []
        for n in nums:
            if len(h) < k:
                heapq.heappush(h, n)
            elif n > h[0]:
                heapq.heapreplace(h, n)
                #heapq.heappushpop(h, n) should be fine too
        return h[0]

