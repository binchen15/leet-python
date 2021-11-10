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
