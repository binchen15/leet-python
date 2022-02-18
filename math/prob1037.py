class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        
        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False
        
        x0, y0 = points[0]
        x1, y1 = points[1]
        x2, y2 = points[2]
        
        d1 = [x1-x0, y1-y0]
        d2 = [x2-x0, y2-y0]
        
        return d1[0]*d2[1] != d1[1]*d2[0]
