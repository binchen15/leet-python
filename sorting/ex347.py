# top K frequent elements in an array

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        f = {}
        for num in nums:
            f[num] = f.get(num, 0) + 1
        pairs = sorted(f.items(), key = lambda x : x[1], reverse=True)
        return [pairs[i][0] for i in range(k) ]
