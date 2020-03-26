# 1025 Divisor game

# 25% solution
class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        if N == 1:
            return False
        dp = [False] * (N+1)  # assume Fail for all N numbers
        dp[1] = False
        dp[2] = True
        for n in range(3, N+1):
            ds = []  # divisors
            for d in range(1, n//2+1):
                if n % d == 0:
                    ds.append(d)
            #if not ds:
            #    dp[n] = False
            for d in ds:
                if dp[n-d] == False:
                    dp[n] = True
                    break
        return dp[-1]


