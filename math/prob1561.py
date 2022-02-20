class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        
        n = len(piles)
        
        ans = 0
        
        while piles:
            piles.pop()
            ans += piles.pop()    
            piles.pop(0)
        
        return ans

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        n = len(piles)
        ans = 0
        l, r = 0, n - 2
        
        while l < r:
            ans += piles[r]
            l += 1
            r -= 2
        
        return ans
