# 139 Word Break

# knapsack with ordering
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        m = len(wordDict)
        wordDict.sort(key=len)

        # dp[i]: can s[:i] be segmented using the whole wordDict
        n  = len(s)
        dp = [False] * (n+1)
        dp[0] = True  # empty string
        for i in range(1, n+1):  # substring of length i
            for j in range(m):
                word = wordDict[j]
                l = len(word)
                if l > i:
                    break
                else:
                    if s[i-l:i] == word and dp[i-l]:
                        dp[i] = True
                        break
        return dp[n]
                   

