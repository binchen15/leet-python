# coin change 2. 5% solution DP
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        m = len(coins)

        dp = [ [0] * (amount+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1

        for i in range(1, m+1):
            val = coins[i-1]
            for j in range(1, amount+1):
                tmp = 0
                k = j
                while k >= 0:
                    tmp += dp[i-1][k]
                    k -= val

                dp[i][j] = tmp

        return dp[m][amount]

# 50% solution
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        m = len(coins)
        
        dp = [ [0] * (amount+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1
        
        for i in range(1, m+1):
            val = coins[i-1]
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j]
                if j-val >= 0:
                    dp[i][j] += dp[i][j-val]
                
        return dp[m][amount]
