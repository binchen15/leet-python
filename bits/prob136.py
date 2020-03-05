class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        "xor is both communicative and associative"
        ans = 0
        for n in nums:
            ans = ans ^ n
        return ans

