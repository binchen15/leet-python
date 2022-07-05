# Wildcard Matching

# recursion. TLE
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)        
        i, j = 0, 0 # pointers to s, and p
        
        while i < m and j < n:
            if p[j] not in "?*":
                if s[i] != p[j]:
                    return False
                else:
                    j += 1
                    i += 1
            elif p[j] == "?":
                j += 1
                i += 1
            else: # j = "*"
                flag = self.isMatch(s[i+1:], p[j:])
                if flag: # "*" is used to kill s[i]
                    return True
                else:    # "*" is wasted
                    #i += 1
                    j += 1
        
        if i == m and j == n:
            return True
        elif i < m:
            return False
        else: # i == m, j < n
            if set(p[j:]) != set("*"):
                return False
            else:
                return True
            

# 5% DP solution
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)        
        
        # dp[i][j] can p[:i+1] match s[:j+1]
        dp = [ [False] * (m+1) for _ in range(n+1)]
        dp[0][0] = True
        
        for i in range(1, n+1): # first column
            c = p[i-1]
            if c == "*":
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = False
                break
        
        for i in range(1, n+1):
            c = p[i-1] 
            for j in range(1, m+1):
                if c == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif c == "*":
                    dp[i][j] = any(dp[i-1][:j+1])
                else:
                    dp[i][j] = (c == s[j-1]) and dp[i-1][j-1]
                    
        return dp[n][m]
                
# 6% solution. But with O(n) memory 
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)        
        
        # dp[i][j] can p[:i+1] match s[:j+1]
        dp    = [False] * (m+1) 
        dp[0] = True
        
        for i in range(1, n+1):
            c = p[i-1]
            for j in range(m, 0, -1):
                if c == "?":
                    dp[j] = dp[j-1]
                elif c == "*":
                    dp[j] = dp[j] or any(dp[:j]) 
                else:
                    dp[j] = (c == s[j-1]) and dp[j-1]
            if c != "*":
                dp[0] = False
        return dp[m]
                
# timelimit error 1809/1811 cases passed
class Solution:

    @lru_cache(maxsize=None)
    def isMatch(self, s: str, p: str) -> bool:

        m = len(s)
        n = len(p)

        if m == 0:
            return self.helper(p)

        if n == 0:
            return False

        if s[0] == p[0]:
            return self.isMatch(s[1:], p[1:])
        if p[0] == "?":
            return self.isMatch(s[1:], p[1:])

        if p[0] == "*":
            return self.isMatch(s[1:], p) or self.isMatch(s, p[1:])

        return False


    @lru_cache(maxsize=None)
    def helper(self, p):
        """does p match empty string"""

        # either p is empty, or consists solely of "*"

        if not p:
            return True
        s = set(p)
        if len(s) > 1:
            return False
        return "*" in s

# 17% DP solution
class Solution:

    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(p), len(s)

        dp = [ [0] * (n+1) for _ in range(m+1) ]

        dp[0][0] = 1

        for i in range(1, m+1):
            dp[i][0] = self.helper(p[:i])

        for i in range(1, m+1):
            for j in range(1, n+1):
                # p[:i] vs s[:j]
                if p[i-1] == s[j-1] or p[i-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if p[i-1] != "*":
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i][j-1] or dp[i-1][j]

        return dp[m][n]



    def helper(self, p):
        """does p match empty string"""

        # either p is empty, or consists solely of "*"
        if not p:
            return 1
        s = set(p)
        if len(s) > 1:
            return 0
        return 1 if "*" in s else 0

# 50% DP solution
class Solution:

    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(p), len(s)

        dp = [ [0] * (n+1) for _ in range(m+1) ]

        dp[0][0] = 1

        for i in range(1, m+1):
            dp[i][0] = self.helper(p[:i])

        for i in range(1, m+1):
            for j in range(1, n+1):
                # p[:i] vs s[:j]
                if p[i-1] == s[j-1] or p[i-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if p[i-1] != "*":
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i][j-1] or dp[i-1][j]

        return dp[m][n]



    def helper(self, p):
        """does p match empty string"""

        # either p is empty, or consists solely of "*"
        if not p:
            return 1
        return set(p) == set("*")
