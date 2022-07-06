# state machine + dp
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:


        m = len(prices)

        if m < 2 or k == 0:
            return 0

        longs =  [ [0] * m for _ in range(k)]
        shorts = [ [0] * m for _ in range(k)]

        for i in range(k):
            longs[i][0] = -prices[0]

        for j in range(1, m):
            # day j
            for i in range(k):
                if i-1 >= 0:
                    longs[i][j]  = max(longs[i][j-1], shorts[i-1][j-1] - prices[j] )
                else:
                    longs[i][j]  = max(longs[i][j-1], -prices[j] )
                shorts[i][j] = max(shorts[i][j-1], longs[i][j-1] + prices[j] )

        return shorts[k-1][m-1]
