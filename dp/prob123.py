# brute force timelimit error.  202/214 cased passed.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        m = len(prices)

        def helper(i, j):
            """max profit between prices[i:j+1] up to 1 transaction"""
            if i >= m:
                return 0
            if j == i:
                return 0
            n = j-i+1
            dp = [0] * n  # cumulative minimum price
            dp[0] = prices[i]

            for k in range(1, n):
                dp[k] = min(dp[k-1], prices[i+k])

            ans = 0
            for k in range(1, n):
                ans = max(ans, prices[i+k] - dp[k-1])

            return ans


        if m == 1:
            return 0
        if m <= 3:
            return helper(0, m-1)

        # assume m >= 4
        ans = 0 # helper(0, m-1)

        for j in range(1, m):
            p1 = helper(0, j)
            p2 = helper(j+1, m-1)
            ans = max(ans, p1+p2)

        return ans

# refer to https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/802372/Python-O(n)-by-DP-Reduction-w-Visualization
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        m = len(prices)
        
        # by the end of day, am I hold a share or not
        b1_hold = [0] * m
        b1_unhold = [0] * m
        
        b1_hold[0] = -prices[0] 
        
        b2_hold = [0] * m
        b2_unhold = [0] * m
        
        b2_hold[0] = -prices[0]
        
        for i in range(1, m):
            b1_hold[i] = max(b1_hold[i-1],  - prices[i])
            b1_unhold[i] = max(b1_unhold[i-1], b1_hold[i-1] + prices[i])
            b2_hold[i] = max(b2_hold[i-1], b1_unhold[i-1] - prices[i] )
            b2_unhold[i] = max(b2_unhold[i-1], b2_hold[i-1] + prices[i])
            
        return b2_unhold[m-1]
