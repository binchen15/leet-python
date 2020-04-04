# Unique Binary Search Trees.

# used dp
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        dp = [0] * (n+1)  # first one just padding
        dp[0] = 1  
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            # BST using [1,2,...,i] inclusive
            for j in range(1,i+1):  # number used as root 
                l = j - 1
                r = i - j
                dp[i] += dp[l] * dp[r]
                
        return dp[n]
        
