# 1313 Decompress Run-Length Encoded List

class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = len(nums)
        if not m:
            return []
        
        ans = []
        i   = 0
        while i < m - 1:
            ans += [ nums[i+1] ] * nums[i]
            i += 2
        return ans
