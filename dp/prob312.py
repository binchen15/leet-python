# 312 Burst Ballons

# not working....

# Brute Force. TLE
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not n:
            return 0
        if n == 1:
            return nums[0]
        
        ans = [0]
        self.helper(nums, 0, ans)
        return ans[0]
        
    def helper(self, nums, curr, ans):
        if not nums:
            if curr > ans[0]:
                ans[0] = curr
            return        
        m = len(nums)
        if m == 1:
            tot = curr + nums[0]
            if tot > ans[0]:
                ans[0] = tot
            return
        if m == 2:
            tot = curr + nums[0]*nums[1] + max(nums[0], nums[1])
            if tot > ans[0]:
                ans[0] = tot
            return
        self.helper(nums[1:],   curr+nums[0]*nums[1], ans)
        self.helper(nums[:m-1], curr+nums[-2]*nums[-1], ans)
        for i in range(1, m-1):
            self.helper(nums[:i]+nums[i+1:], curr+nums[i-1]*nums[i]*nums[i+1], ans)


# Jul 8 2022
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]

        self.ans = 0

        def walk(arr, score):
            if not arr:
                self.ans = max(self.ans, score)
                return

            for i, v in enumerate(arr):
                tmp = v
                if i >= 1:
                    tmp *= arr[i-1]
                if i < len(arr) - 1:
                    tmp *= arr[i+1]

                arr2 = arr[:i] + arr[i+1:]
                walk(arr2, score+tmp)

        walk(nums, 0)
        return self.ans
# July 8. one more case passed
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]

        self.ans = 0

        def walk(arr, score):
            if not arr:
                self.ans = max(self.ans, score)
                return

            if len(arr) == 1:
                self.ans = max(self.ans, score + arr[0])
                return

            if len(arr) == 2:
                self.ans = max(self.ans, score + arr[0]*arr[1] + max(arr[0], arr[1]) )
                return

            for i, v in enumerate(arr):
                tmp = v
                if i >= 1:
                    tmp *= arr[i-1]
                if i < len(arr) - 1:
                    tmp *= arr[i+1]

                arr2 = arr[:i] + arr[i+1:]
                walk(arr2, score+tmp)

        walk(nums, 0)
        return self.ans

# worry about the last ballon to burst, instead of first
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        nums = [1] + nums + [1]

        @lru_cache(maxsize=None)
        def helper(i, j):
            """nums[i, j+1]"""
            ans = 0
            for k in range(i+1, j):
                ans = max(ans, helper(i, k) + helper(k, j) + nums[i] * nums[k] * nums[j])
            return ans

        return helper(0, len(nums)-1)

# DP solution. same recursion as above. 60%
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        nums = [1] + nums + [1]

        n = len(nums)

        dp = [ [0] * n for _ in range(n) ]

        for delta in range(2, n):
            for i in range(n-delta):
                j = i + delta
                tmp = 0
                for k in range(i+1, j):
                    tmp = max(tmp, dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])

                dp[i][j] = tmp

        return dp[0][n-1]
