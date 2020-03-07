# missing and duplicates in an array
# 95%
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d   = {}
        ans = []
        ub  = 1
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
                ans.append(n)  # found the dup.
            if n > ub:
                ub = n
        i = 1
        while i <= ub:
            if i not in d:
                ans.append(i)  # found the missing
                break
            i += 1
        if len(ans) == 1:
            ans.append(ub+1)
        return ans
                
        
