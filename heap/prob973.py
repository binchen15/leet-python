#K Closest Points to Origin
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        import heapq
        return heapq.nsmallest(K, points, 
            key=lambda x: x[0]*x[0] + x[1]*x[1])

class Solution(object):
    """27% percentile"""
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        import heapq
        hp = []  # max heap K smallest -distance
        ds = {}
        for p in points:
            d = p[0]*p[0] + p[1]*p[1]
            if len(hp) < K:
                heapq.heappush(hp, -d)
            elif d < -hp[0]:
                heapq.heapreplace(hp, -d)
            if -d in ds:
                ds[-d].append(p)
            else:
                ds[-d] = [p]
        ans = []
        for d in hp: # negated d
            ans.append(ds[d].pop())
        return ans
        
