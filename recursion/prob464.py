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

# bitmask 
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        N = maxChoosableInteger
        if (N*(N+1)/2) < desiredTotal:
            return False

        if N >= desiredTotal:
            return True

        memo = {}
        mask = int("1"*N, 2)

        def helper(total, mask):

            if mask == 0: # no numbers left
                return total == 0

            if (total, mask) in memo:
                return memo[(total, mask)]

            for i in range(1, N+1):
                if (mask >> (i-1)) & 1 == 0:  # used already
                    continue
                if i >= total:
                    memo[(total, mask)] = True
                    return True

                if not helper(total-i, mask - (1 << (i-1)) ):
                    memo[(total, mask)] = True
                    return True
            memo[(total, mask)] = False

            return False

        return helper(desiredTotal, mask)

# @LRU_Cache
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        N = maxChoosableInteger
        if (N*(N+1)/2) < desiredTotal:
            return False

        mask = int("1"*N, 2)

        @lru_cache(None)
        def helper(total, mask):

            if mask == 0: # no numbers left
                return total == 0

            for i in range(1, N+1):
                if (mask >> (i-1)) & 1 == 0:  # used already
                    continue
                if i >= total:
                    return True

                if not helper(total-i, mask - (1 << (i-1)) ):
                    return True

            return False

        return helper(desiredTotal, mask)

