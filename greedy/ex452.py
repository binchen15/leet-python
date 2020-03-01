class Solution(object):
    """minimum arrow to burst all ballons"""
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        m = len(points)
        if m <= 1:
            return m
        points.sort(key=lambda x : x[1])
        c = 1 # counter: number of arrows needed
        x = points[0][1] # burst first, and max potential to burst others
        for i in range(1, m):
            if points[i][0] <= x:
                continue # current arrow still bursts it
            else:
                c += 1           # need new arrow
                x = points[i][1] # aim of new arrow
        return c
        
        
