# 1004 Max Consecutive Ones III

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        n = len(nums)
        l, r = 0, 0
        cnt = 0
        res = 0

        while r < n:
            if cnt < k:
                if nums[r] == 0:
                    cnt += 1
                r += 1
            elif nums[r] == 1:
                r += 1
            else:
                if nums[l] == 0:
                    cnt -= 1
                l += 1
            res = max(res, r-l)

        return res
