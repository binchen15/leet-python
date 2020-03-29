# 518 Coin Change II.

# in order, in-place traversal

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount < 0:
            return 0
        if amount == 0:
            return 1
        
        m  = len(coins)
        dp = [0] * (amount+1)
        dp[0] = 1
        for i in range(1, m+1):
            v = coins[i-1] # face value
            for j in range(v, amount+1):
                #n = j // v
                # old dp[j] was for k == 0
                dp[j] += dp[j-v]
        return dp[amount]
                    
