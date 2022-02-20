class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        def helper(point, query):
            """test if point if within the ciricel given by query"""
            
            dx, dy = point[0] - query[0], point[1] - query[1]
            return dx * dx + dy * dy <= query[2] * query[2]
        
        ans = []
        
        for query in queries:
            cnt = 0
            for point in points:
                if helper(point, query):
                    cnt += 1
            ans.append(cnt)
            
        return ans
