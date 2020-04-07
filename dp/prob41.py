# 41 First Missing Positive
# Your algorithm should run in O(n) time and uses constant extra space.

# 5% bad solution
# O(n) in space. not good
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        a = [0] * (m+1)
        for n in nums:
            if 1 <= n <= m:
                a[n] = 1
        for j in range(1, m+1):
            if not a[j]:
                return j
        return m + 1
       
# 5% solution.
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        nums.append(0)
        for i in range(m):
            v = nums[i]
            if v == i:
                continue
            while 1 <= v <= m and v != nums[v]:
                tmp = nums[v]
                nums[v] = v
                v = tmp
        for i in range(1,m+1):
            if nums[i] != i:
                return i
        return m + 1
                
 
