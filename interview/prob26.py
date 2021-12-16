class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)
        if n <= 1:
            return n

        r = n-1
        while r > 0:
            if nums[r] == nums[r-1]:
                nums.pop(r)
            r -= 1

        return len(nums)

