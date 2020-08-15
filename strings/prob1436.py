# 1436 Destination city

class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        starts = set()
        ends = set()
        for path in paths:
            starts.add(path[0])
            ends.add(path[1])
        diff = ends.difference(starts)
        return list(diff)[0]
