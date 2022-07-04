# 983 Minimum Cost for tickets

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        n = len(days)

        dp = [0] * n
        dp[0] = min(costs)  # not costs[0]

        def helper(i, delta):
            """trace from days[i] backward for j such that distanc  within delta"""
            j = i
            while j-1 >= 0 and days[i] - days[j-1] < delta:
                j -= 1
            return j

        for i in range(1, n):
            c1 = dp[i-1] + costs[0]
            j2 = helper(i, 7)
            j3 = helper(i, 30)
            if j2-1 >= 0:
                c2 = dp[j2-1] + costs[1]
            else:
                c2 = costs[1]
            if j3-1 >= 0:
                c3 = dp[j3-1] + costs[2]
            else:
                c3 = costs[2]
            dp[i] = min(c1, c2, c3)

        return dp[n-1]
