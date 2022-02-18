class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        cnts = {}
        
        for v in deck:
            cnts[v] = cnts.get(v, 0) + 1
            
        values = list(cnts.values())
        
        if min(values) == 1:
            return False
        
        n = len(values)
        
        for i in range(1, n):
            values[0] = math.gcd(values[0], values[i])
            
            
        return values[0] > 1
