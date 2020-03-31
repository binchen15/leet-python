# 3 Longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = len(s)
        if m <= 1:
            return m
        
        # dp[i] longest substring ends at s[i]
        dp = [0] * m
        dp[0] = 1
        ub    = 1
        for i in range(1, m):
            c = s[i]
            p = s[i-dp[i-1]:i]
            if c not in p:
                dp[i] = dp[i-1] + 1
            else:
                j = p.rindex(c)
                dp[i] = dp[i-1]-j
            ub = max(ub, dp[i])
        return ub
        
  
