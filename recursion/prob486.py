# https://leetcode.com/problems/predict-the-winner/discuss/414803/Python-AC-98-Both-Recursion-and-DP-with-detailed-explanation.

# 10% solution
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def helper(i, j):
            """calculate margin of current player for nums[i:j+1]"""
            
            if i == j:
                return nums[i]
            
            margin = max(nums[i]-helper(i+1, j), nums[j]-helper(i, j-1))
            
            return margin
        
        return helper(0, len(nums)-1) >= 0

# 30% solution
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        memo = {}

        def helper(i, j):
            """calculate margin of current player for nums[i:j+1]"""

            if i == j:
                return nums[i]

            if (i, j) in memo:
                return memo[(i, j)]

            margin = max(nums[i]-helper(i+1, j), nums[j]-helper(i, j-1))
            memo[(i,j)] = margin

            return margin

        return helper(0, len(nums)-1) >= 0

# dp solution
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        n = len(nums)

        dp = [ [0] * n for _ in range(n) ]
        # dp[i][j] stores the margin of current player for subarray nums[i:j+1]
        for i in range(n):
            dp[i][i] = nums[i]

        for d in range(1, n):
            for i in range(n-d):
                j = i + d
                margin = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
                dp[i][j] = margin

        return dp[0][n-1] >= 0

