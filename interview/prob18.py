# 18 4Sum

# Two pointers
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        m = len(nums)
        if m < 4:
            return []
        nums.sort()
        
        ans = []
        i = 0
        while i < m-3:
            a = nums[i]
            j = i + 1
            while j < m-2:
                b = nums[j]
                t = target - (a+b)
                l, r = j+1, m-1
                while l < r:
                    c, d = nums[l], nums[r]
                    if c+d > t:
                        r -= 1
                    elif c+d < t:
                        l += 1
                    else:
                        ans.append([a,b,c,d])
                        l += 1
                        r -= 1
                        while l < m and nums[l] == c:
                            l += 1
                        while r >= 0 and nums[r] == d:
                            r -= 1
                j += 1
                while j < m and nums[j] == b:
                    j += 1
            i += 1
            while i < m and nums[i] == a:
                i += 1
        return ans
            

