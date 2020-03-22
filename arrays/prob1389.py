# 1389 Creat Target Array in given order

class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        ans = []
        for i, j in enumerate(index):
            ans.insert(j, nums[i])
        return ans
