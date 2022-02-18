class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        n = len(coordinates)
        if n == 2:
            return True
        
        diff = []
        
        for i in range(n-1):
            nxt = coordinates[i+1] 
            cur = coordinates[i]
            dxy = (nxt[0] - cur[0], nxt[1] - cur[1]) 
            diff.append(dxy)
            
        for i in range(n-2):
            cur = diff[i]
            nxt = diff[i+1]
            
            if cur[0]*nxt[1] != cur[1]*nxt[0]:
                return False
            
        return True
