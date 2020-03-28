# 494 Target Sum

#dp[i][j] the number of ways to get sum to j using nums[:i+1]
# maximum of j is sum(nums)
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        m = len(nums)
        S = abs(S)  # mirror symmetry
        n = sum(nums)
        if S > n:
            return 0
        dp = [ [0] * (n+1) for _ in range(m)]
        
        # initialize the first non-trivial row
        v = nums[0]
        for j in range(n+1):
            if v == j:
                if v > 0:
                    dp[0][j] = 1
                else:
                    dp[0][j] = 2
                     
        for i in range(1, m):
            v = nums[i]   
            for j in range(n+1):
                if v == 0:   # (+/- 0)
                    dp[i][j] = 2 * dp[i-1][j]
                else:
                    s = j - v # used mirror symmetry again
                    t = j + v
                    dp[i][j] = dp[i-1][abs(s)]
                    if t <= n:
                        dp[i][j] += dp[i-1][t]
        return dp[m-1][S]
            
