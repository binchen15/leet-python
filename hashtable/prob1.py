class Solution(object):
    """twoSum O(n), hash set"""
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        uniq = set(nums)
        for m in uniq:
            n = target - m
            if n in uniq:
                if n != m:
                    return [nums.index(m), nums.index(n)]
                else:
                    i1 = nums.index(m)
                    return [i1, nums.index(n, i1+1)]
                    
