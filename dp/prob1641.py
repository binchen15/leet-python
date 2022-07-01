
# Count Sorted Vowel Strings

class Solution:
    def countVowelStrings(self, n: int) -> int:

        if n == 1:
            return 5

        dp = [ [0] * (n+1) for _ in range(6)]

        for i in range(6):
            dp[i][0] = 1

        for i in range(1, 6):
            for j in range(1, n+1):
                dp[i][j] = sum(dp[i-1][:j+1])

        return dp[5][n]
