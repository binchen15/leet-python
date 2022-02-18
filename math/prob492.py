class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        ub = int(math.sqrt(area))
        
        if ub * ub == area:
            return [ub, ub]
        
        for i in range(ub+1, area+1):
            if area % i == 0:
                return [i, area // i]
        
