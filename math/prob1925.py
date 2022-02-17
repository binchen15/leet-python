class Solution:
    def countTriples(self, n: int) -> int:
        
        ans = set()
        
        m = {i*i : i for i in range(1, n+1)}
        
        for sq1 in m:
            for sq2 in m:
                if sq1 + sq2 in m:
                    ans.add((m[sq1], m[sq2], m[sq1+sq2]))                    
                        
        return len(ans)
