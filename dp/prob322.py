# Prob. 322 Coin change

# DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            col = []
            for c in coins:
                if i-c >= 0 and dp[i-c] != -1:
                    col.append(dp[i-c]+1)
            if col:
                dp[i] = min(col)

        return dp[amount]

# top down recursion with memoization
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0
        if amount < 0:
            return -1

        memo = {}

        def helper(coins, amount):

            if amount == 0:
                return 0
            if amount < 0:
                return -1
            if amount in memo:
                return memo[amount]

            candidates = []
            for c in coins:
                if amount - c >= 0:
                    tmp = helper(coins, amount - c)
                    if tmp != -1:
                        candidates.append(tmp + 1)
            if not candidates:
                ans = -1
            else:
                ans = min(candidates)
            memo[amount] = ans
            return ans

        return helper(coins,amount)
