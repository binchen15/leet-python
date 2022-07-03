#Brute force. Time limit error

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:

        def isFair(arr):
            """ nums[i:j+1] is fair?"""
            n = len(arr)
            ev, od  = 0, 0
            for k in range(0, n, 2):
                ev += arr[k]
            for k in range(1, n, 2):
                od += arr[k]

            return 1 if ev == od else 0

        ans  = 0
        n = len(nums)

        for i in range(n):
            ans += isFair(nums[:i] + nums[i+1:])

        return ans

# 2 1-D DP array
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return 1

        dp = [0] * n
        dp[0], dp[1] = nums[0], nums[1]
        for i in range(2, n):
            dp[i] = nums[i] + dp[i-2]

        dp2 = [0] * n
        dp2[-1], dp2[-2] = nums[-1], nums[-2]
        for i in range(n-3, -1, -1):
            dp2[i] = nums[i] + dp2[i+2]

        ans = 0

        for i in range(n):
            # remove nums[i]
            tmp1, tmp2 = 0, 0
            if i-1 >= 0:
                tmp1 += dp[i-1]
            if i+2 < n:
                tmp1 += dp2[i+2]
            if i-2 >= 0:
                tmp2 += dp[i-2]
            if i+1< n:
                tmp2 += dp2[i+1]
            if tmp1 == tmp2:
                ans += 1

        return ans
