# 1143 Longest common subseqence

def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        if not m or not n:
            return 0
        
        #dp[i][j] for text1[:i+1] vs text2[:j+1]
        dp = [ [0] * (n+1) for _ in range(m+1) ]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
                              

