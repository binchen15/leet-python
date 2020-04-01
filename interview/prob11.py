# 11 Container with most water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        vol = 0
        m   = len(height)
        l, r = 0, m-1
        while l < r:
            hl, hr = height[l], height[r]
            v = min(hl, hr)*(r-l)
            vol = max(vol, v)
            if hl < hr:
                l += 1
            else:
                r -= 1
        return vol
        


