# 448 Find all numbers disappered in an array

#85% in time. but 11% in memory
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n    = len(nums)
        uniq = set(nums)
        ans  = []
        for i in range(1,n+1):
            if i not in uniq:
                ans.append(i)
        return ans


