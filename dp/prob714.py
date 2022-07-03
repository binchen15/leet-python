# wrong trading strategy. wrong solution
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        n = len(prices)
        if n <= 1:
            return 0

        profit = 0
        l, r = 0, 0
        while l < n:

            # identify an up trend
            while r+1 < n and prices[r+1] - prices[r] > 0:
                r += 1

            if r > l:
                diff = prices[r] - prices[l] - fee
                profit += max(diff, 0)
                l = r + 1
                r = l
            else:
                l += 1
                r = l

        return profit

# DP solution
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        n = len(prices)
        if n <= 1:
            return 0

        # max profix for prices[i:]
        dp0 = [0] * (n+1) # no stock at beginning of the day
        dp1 = [0] * (n+1) # hold one share at the beginning of the day

        for i in range(n-1, -1, -1):
            if i == n-1:
                dp0[i] = dp0[i+1]
                dp1[i] = prices[i] - fee + dp0[i+1]
            else:
                dp0[i] = max(-prices[i] + dp1[i+1], dp0[i+1])
                dp1[i] = max(prices[i] - fee + dp0[i+1], dp1[i+1])

        return dp0[0]
