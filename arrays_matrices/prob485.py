class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m == 0:
            return 0
        
        rec = 0
        i = 0
        while i < m:
            while i < m and nums[i] == 0: # find next 1
                i += 1
            if i == m:
                break
            j = i
            cnt = 0
            while j < m and nums[j] == 1:
                cnt += 1
                j   += 1
            if cnt > rec:
                rec = cnt
            if j == m:
                break
            i = j + 1   # nums[j] must be 0
                
        return rec
        
