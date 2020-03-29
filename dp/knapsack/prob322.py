# 322 Coin Chain
# complete knapsack problem

# timelimit error
# reverse order traversal..
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        
        m = len(coins)
        
        dp = [0]*(amount+1) 
        for j in range(1, amount+1): # init with no coins available
            dp[j] = -1
        for i in range(1, m+1):
            val = coins[i-1] # face value
            for j in range(amount, val-1, -1):
                n = j // val # upper bound
                tmp = dp[j]  # cuerrent minimum without val
                for k in range(1, n+1): 
                    if dp[j-k*val] != -1:
                        if tmp == -1:
                            tmp = dp[j-k*val] + k
                        else:
                            tmp = min(tmp, dp[j-k*val] + k)
                dp[j] = tmp
            
        return dp[amount] 

# inorder traversal
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        
        m = len(coins)
        
        dp = [0]*(amount+1) 
        for j in range(1, amount+1): # init with no coins available
            dp[j] = -1
        for i in range(1, m+1):
            val = coins[i-1] # face value
            if val <= amount:
                dp[val] = 1
            for j in range(val+1, amount+1):
                if dp[j-val] != -1:
                    if dp[j] == -1:
                        dp[j] = dp[j-val] + 1
                    else:
                        dp[j] = min(dp[j], dp[j-val] + 1)
                
        return dp[amount] 
        
