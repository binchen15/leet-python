# buggy one 
# 20% solution
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        if (maxChoosableInteger * (maxChoosableInteger + 1) / 2) < desiredTotal:
            return False

        memo = {}
        bags = {i for i in range(1, maxChoosableInteger+1)}

        def helper(total, bags):

            if not bags:
                return total == 0

            if (tuple(bags), total) in memo:
                return memo[(tuple(bags), total)]

            if max(bags) >= total:
                memo[(tuple(bags), total)] = True
                return True

            for val in bags:
                if not helper(total-val, bags.difference({val})):
                    memo[(tuple(bags), total)] = True
                    return True
            memo[(tuple(bags), total)] = False

            return False

        return helper(desiredTotal, bags)

