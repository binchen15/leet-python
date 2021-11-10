# 139 Word Break

# DFS + memoization
# timeout if no memoization
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = {}
        n = len(s)

        def helper(s, cur, words, memo, n):
            """if s[cur:] can be segmented"""
            if cur >= n:
                return True
            if cur in memo:
                return memo[cur]
            for word in words:
                if cur+len(word) <= n and s[cur: cur+len(word)] == word:
                    if helper(s, cur+len(word), words, memo, n):
                        memo[cur] = True
                        return True
            memo[cur] = False
            return False

        return helper(s, 0, words, memo, n)

# DP solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        dp = [False] * (n+1)  # dp[i] store result for s[:i]
        dp[0] = True
        for i in range(n+1):
            if dp[i]:
                for word in wordDict:
                    if i + len(word) <= n and s[i:i+len(word)] == word:
                        dp[i+len(word)] = True
        return dp[-1]

# BFS + visited set
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        q = [0]
        visited = set()

        while q:
            cur = q.pop(0)
            if cur in visited:
                continue
            visited.add(cur)
            if cur == n:
                return True
            for word in wordDict:
                t = cur + len(word)
                if t <= n and s[cur:t] == word:
                    q.append(t)

        return False
