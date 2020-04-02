# 15. 3Sum

# Brutal force solution. TLE
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        m = len(nums)
        if m < 3:
            return []
        myset = set()
        for i in range(m-2):
            for j in range(i+1, m-1):
                for k in range(j+1, m):
                    if nums[i] + nums[j] + nums[k] == 0:
                        t = tuple(sorted([nums[i],nums[j],nums[k]]))
                        myset.add(t)
                        
        ans = [ list(t) for t in myset]
        return ans

# two pointers colliding. 80% solution
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        m = len(nums)
        if m < 3:
            return []
        nums.sort()
        ans = []
        i   = 0
        while i < m-2:
            a = nums[i]
            tgt = -a # b + c
            l, r = i+1, m-1
            while l < r:
                if nums[l] + nums[r] > tgt:
                    r -= 1
                elif nums[l] + nums[r] < tgt:
                    l += 1
                else:
                    b, c = nums[l], nums[r]
                    ans.append([a,b,c])
                    l += 1
                    r -= 1
                    while l < m and nums[l] == b:
                        l += 1
                    while r >= 0 and nums[r] == c:
                        r -= 1
            i += 1
            while i < m and nums[i] == a:
                i += 1
        return ans
                        
                     
