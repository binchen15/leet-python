class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        ans = 0
        
        n = len(points)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    A = points[i]
                    B = points[j]
                    C = points[k]
                    area = self.findArea(A, B, C)
                    if area > ans:
                        ans = area
                        
        return ans
        
    def findArea(self, A, B, C):
        
        AB = (B[0] - A[0], B[1] - A[1])
        AC = (C[0] - A[0], C[1] - A[1])
        
    
        def len(v):
            return math.sqrt(v[0]*v[0] + v[1]*v[1])
        
        def inner(v1, v2):
            return v1[0]*v2[0] + v1[1]*v2[1]
        
        l1 = len(AB)
        l2 = len(AC)
        # rad = math.acos(inner(AB, AC) / (l1 * l2))
        # area = 0.5 * l1 * l2 * math.sin(rad)
        cs = inner(AB, AC) / (l1 * l2)
        sn = math.sqrt(abs(1 - cs*cs))
        
        area = 0.5 * l1 * l2 * sn
                        
        return area

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        ans = 0
        
        n = len(points)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    A = points[i]
                    B = points[j]
                    C = points[k]
                    area = self.findArea(A, B, C)
                    if area > ans:
                        ans = area
                        
        return ans
        
    def findArea(self, A, B, C):
        
        AB = (B[0] - A[0], B[1] - A[1])
        AC = (C[0] - A[0], C[1] - A[1])
        
        def len(v):
            return math.sqrt(v[0]*v[0] + v[1]*v[1])
        
        def inner(v1, v2):
            return v1[0]*v2[0] + v1[1]*v2[1]
        
        l1 = len(AB)
        l2 = len(AC)
        
        cs = inner(AB, AC) / (l1 * l2)
        if cs > 1:
            cs = 1
        elif cs < -1:
            cs = -1
        rad = math.acos(cs)
        area = 0.5 * l1 * l2 * math.sin(rad) 
        
        return area
