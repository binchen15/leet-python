# 202 Happy number

class Solution:
    def isHappy(self, n: int) -> bool:

        history = set()

        memo = {}

        def helper(n):
            if n in memo:
                return memo[n]
            ans = str(sum(map(lambda x : int(x)**2, str(n))))
            memo[n] = ans
            return ans

        if n == 1:
            return True

        while True:
            n = helper(n)
            if n == "1":
                return True
            elif n in history:
                return False
            else:
                history.add(n)

