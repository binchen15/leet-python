# 322 coin change

# BFS
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        
        currL = [amount]
        nextL = set()
        level = 0  # number of coins
        while currL:
            while currL:
                val = currL.pop(0)
                if val == 0:
                    return level
                else:
                    for coin in coins:
                        if val - coin >= 0:
                            nextL.add(val-coin)                
            currL = list(nextL)
            nextL = set()
            level += 1
        return -1
                
