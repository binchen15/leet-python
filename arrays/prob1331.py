# 1331 Rank Transform of an array

class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if not arr:
            return []
        vals = sorted(list(set(arr)))
        ranks = { v : i+1 for i, v in enumerate(vals) }
        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]
        return arr

