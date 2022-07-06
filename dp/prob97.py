# 97 Interleaving String

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        from collections import Counter
        if Counter(s1+s2) != Counter(s3):
            return False
        
        m, n = len(s3), len(s1)  # m = n + q
        q    = len(s2)
        # dp[i][j] can s3[:i] be formed by s1[:j] and s2[:i-j]
        dp = [ [False] * (n + 1) for _ in range(m+1) ]
        dp[0][0] = True
        for i in range(1, q+1): # interleaving("", s2) => s3
            dp[i][0] = dp[i-1][0] and (s2[i-1] == s3[i-1])
            
        for i in range(1, m+1):
            ub = min(i+1, n+1)
            for j in range(1, ub): # j <= min(i, n)
                #a = s1[:j]
                #b = s2[:i-j]
                #c = s3[:i]
                #if s3[i-1] != s1[j-1] and
                #   s3[i-1] != s2[i-j-1]:
                #        dp[i][j] = False
                c = s3[i-1]
                if (c == s1[j-1] and dp[i-1][j-1]) or \
                   ( (0 <= i-j-1 < q) and \
                      c == s2[i-j-1] and dp[i-1][j] ):
                        dp[i][j] = True
                        
        return dp[m][n]       
                

# recursion + memo
class Solution:

    @lru_cache(maxsize=None)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n1 + n2 != n3:
            return False

        if n1 == 0 or n2 == 0:
            return s1 + s2 == s3

        if s1[-1] != s3[-1] and s2[-1] != s3[-1]:
            return False

        if s1[-1] == s3[-1]:
            if self.isInterleave(s1[:n1-1], s2, s3[:n3-1]):
                return True

        if s2[-1] == s3[-1]:
            if self.isInterleave(s1, s2[:n2-1], s3[:n3-1]):
                return True

        return False
