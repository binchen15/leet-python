# 1266 Minimum time visiting all points

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        m = len(points)
        if m == 1:
            return 0
        time = 0
        for i in range(m-1):
            dx = abs(points[i+1][0] - points[i][0])
            dy = abs(points[i+1][1] - points[i][1])
            time += max(dx, dy)
        return time

