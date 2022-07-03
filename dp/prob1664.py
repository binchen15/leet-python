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
