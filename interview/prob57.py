# 57 Insert Intervals

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        m = len(intervals)
        if not m:
            intervals.append(newInterval)
            return intervals

        a = newInterval[0]
        b = newInterval[1]
        
        # is newInterval interior to any interval
        # if so, nothing to do
        for i in range(m):
            p0, p1 = intervals[i]
            if p0 <= a and b <= p1:
                return intervals
        
        l = m  # chaning length of intervals
        i = 0
        while i < l:
            p0, p1 = intervals[i]
            if a <= p0 and p1 <= b: # drop interiors
                del intervals[i]
                l -= 1
            elif p0 <= a <= p1:
                a = p0 # left extend newInterval
                del intervals[i]
                l -= 1
            elif p0 <= b <= p1:
                b = p1 # right extend newInterval
                del intervals[i]
                l -= 1
            else:
                i += 1
                
        intervals.append([a,b])
        intervals.sort()
        return intervals
            
