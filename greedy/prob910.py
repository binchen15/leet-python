# https://leetcode.com/problems/smallest-range-ii/discuss/2026259/In-Depth-Explanation
# https://practice.geeksforgeeks.org/problems/minimize-the-heights-i/1/?page=1&category[]=Greedy&sortBy=submissions

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:

        n = len(nums)
        if n == 1:
            return 0

        nums.sort()

        if k >= nums[n-1] - nums[0]:
            return nums[n-1] - nums[0]

        ans = nums[n-1] - nums[0]

        # nums[:i+1] goes up. nums[i+1:] goes down
        for i in range(n-1):
            Mx = max(nums[n-1]-k, nums[i]+k)
            mx = min(nums[0] + k, nums[i+1]-k)
            ans = min(ans, Mx - mx)

        return ans
