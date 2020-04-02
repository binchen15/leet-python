# 16 3Sum Closest

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        m   = len(nums)
        nums.sort()
        ans = nums[0] + nums[1] + nums[m-1] 
        d   = abs(ans - target)
        for i in range(m-2):
            a = nums[i]
            l, r = i+1, m-1
            while l < r:
                t = a + nums[l] + nums[r]
                if t > target:
                    r -= 1
                else:
                    l += 1
                d2 = abs(t-target)
                if d2 < d:
                    ans = t
                    d   = d2
            i += 1
        return ans
            

