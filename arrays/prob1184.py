# 1184 Distance between bus stops

class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        m = len(distance)
        if m == 1 or start == destination:
            return 0
        if start > destination:
            start, destination = destination, start
        d1 = sum(distance[start:destination])
            
        d2 = sum(distance[destination:]) + sum(distance[:start])
        return min(d1, d2)
    
