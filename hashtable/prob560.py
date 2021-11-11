# Prob. 560 Subarray Sum Equals K

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)

        hmap = collections.defaultdict(int)  # sum -> count
        hmap[0] = 1

        cnt = 0
        csum = 0 # cumulative sum
        for i in range(n):
            csum += nums[i]
            if csum - k in hmap:
                cnt += hmap[csum-k]
            hmap[csum] += 1
        return cnt
