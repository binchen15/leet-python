class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        n, r = divmod(n, 2)
        
        ans = []
        for i in range(1, n+1):
            ans.extend([i, -i])
        if r:
            ans.append(0)
            
        return ans
