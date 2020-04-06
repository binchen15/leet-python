# 38 Count and Say

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        dp = [""] * max(n+1, 6)
        dp[:6] = ["", "1", "11", "21", "1211", "111221"]
        if n <= 5:
            return dp[n]
        for i in range(6, n+1):
            prev = dp[i-1]  # previous word
            m    = len(prev)
            j    = 0
            say  = ""
            while j < m:
                c   = prev[j]
                cnt = 1
                while j+1 < m and prev[j+1] == c:
                    cnt += 1
                    j   += 1
                say += "{}{}".format(cnt, c)
                j += 1
            dp[i] = say
            
        return dp[n]
                    
                
                
