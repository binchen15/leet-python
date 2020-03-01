class Solution(object):
    """greedy algorithm"""
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) <= 1:
            return 0 
        # sorting using the upper bound
        intervals.sort(key = lambda x : x[1])
        c   = 1 # number of intervals kept
        m   = len(intervals) 
        end = intervals[0][1] 
        for j in range(1, m):
            if intervals[j][0] < end:  # intersect
                continue  # drop
            end = intervals[j][1]
            c   += 1  # keep
        return m - c
        
