# two pointers
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        if n <= 1:
            return 0
        
        profit = 0
        l, r = 0, 0
        while l < n:
            
            while r + 1 < n and prices[r+1] > prices[r]:
                r += 1
            if r > l:
                profit += prices[r] - prices[l]
                l = r + 1
                r = l
            else:
                l += 1
                r = l
                
        return profit
