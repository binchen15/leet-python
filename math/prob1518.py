class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        full = numBottles
        empty = 0
        ans = 0
        
        while full > 0 or empty >= numExchange:
            ans += full  # drink water 
            empty += full
            full, empty = divmod(empty, numExchange)
            
        return ans
