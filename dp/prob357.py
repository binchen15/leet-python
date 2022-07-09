# brute force solution
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        cnts = 0
        for i in range(10**n):
            if len(str(i)) == len(set(str(i))):
                cnts += 1
        return cnts

# Count numbers with unique digits
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        dp = [0] * (n+1)
        dp[0] = 1

        def helper(n, m):
            ans = 1
            for i in range(n, n-m, -1):
                ans *= i
            return ans

        for i in range(1, n+1):
            dp[i] = dp[i-1] + 9 * helper(9, i-1)

        return dp[n]
