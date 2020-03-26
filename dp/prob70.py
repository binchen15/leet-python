# prob. 70 Climbing Stairs 

# memoization, bottom up
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        memo = [0] * (n+1)
        memo[1] = 1
        memo[2] = 2
        for i in range(3, n+1):
            memo[i] = memo[i-2] + memo[i-1]
        return memo[n]

# iteration
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        # dp[i] = dp[i-1] + dp[i-2]
        prev  = 1
        curr  = 2
        for _ in range(n-2):
            curr, prev = curr+prev, curr
        return curr

