class Solution(object):
    """O(n^2) time limit error"""
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m  = len(nums)
        #ub = m - 1
        for i in range(m-1):
            for j in range(i+1, m):
                if nums[i] == nums[j]:
                    return nums[i]


class Solution(object):
    """bisect method"""
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        l = 1
        r = m - 1  # maximum value n of [1, n]
        
        while l <= r:
            mid = l + (r - l) // 2
            cnt = 0   # number of vals <= mid
            for v in nums:
                if v <= mid:
                    cnt += 1
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid - 1
        return l
        
