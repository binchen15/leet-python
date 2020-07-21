class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [ nums[0] ]
        for n in nums[1:]:
            result.append(n+result[-1])
        return result

