# 56 Merge Intervals (Medium)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(intervals)
        if m <= 1:
            return intervals
        intervals.sort()
        
        i = 0
        l = m
        while i < l:
            if i + 1 < l and intervals[i+1][0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                del intervals[i+1]
                l -= 1
            else:
                i += 1
        return intervals
