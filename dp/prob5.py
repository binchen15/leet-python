# 5 longest palindrome

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1:
            return s

        dp = [ [False] * n for _ in range(n)]
        record = [1, [0,0]]  # index for the longest palindrome, and length

        for i in range(n):
            dp[i][i] = True
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                record = [2, [i, i+1]]
        if n > 2:
            for l in range(2, n):
                for i in range(0, n-l):
                    if dp[i+1][i+l-1] and s[i] == s[i+l]:
                        dp[i][i+l] = True
                        if l + 1 > record[0]:
                            record[0] = l + 1
                            record[1] = [i, i+l]


        start, end = record[1]
        return s[start:end+1]

# Jun 28 2022
class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        if n <= 1:
            return s

        ans = s[0]
        size = 1

        memo = [[0] * n for _ in range(n)]
        for i in range(n):
            memo[i][i] = 1

        for delta in range(1, n):
            for i in range(n - delta):
                j = i + delta
                if s[i] != s[j]:
                    continue
                if i+1 == j or memo[i+1][j-1] == 1:
                    memo[i][j] = 1
                    if j-i+1 > size:
                        size = j-i+1
                        ans = s[i:j+1]

        return ans

