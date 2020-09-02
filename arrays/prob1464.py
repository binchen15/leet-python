# Maximum Product of Two Elements in an Array

# 3 methods, from O(n*log(n)) to o(n)

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums_sorted = sorted(nums, reverse=True)
        # return (nums_sorted[0]-1)*(nums_sorted[1]-1)
        # method 2
        # n1 = max(nums)
        # nums[nums.index(n1)] = -1
        # n2 = max(nums)
        # return (n1-1) * (n2-1)
        n1 = -1
        n2 = -1
        for n in nums:
            if n > n1:
                n2 = n1
                n1 = n
            elif n > n2:
                n2 = n
        return (n1-1) * (n2-1)
