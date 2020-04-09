# 746. Min Cost Climbing Stairs

# 60 percent solution
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n  = len(cost)
        # dp[i] the min cost to reach step i
        # reach is not crossing, so need reach stair n, not n-1
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n+1):
            dp[i] = min(dp[i-2] + cost[i-2], # two step from i-2 
                        dp[i-1] + cost[i-1]  # one step from i-1
                       )
        return dp[n]
        
