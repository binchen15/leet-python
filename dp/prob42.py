# 42 Trapping Rain Water

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m = len(height)
        if m <= 1:
            return 0
        lmax = [0] * m
        rmax = [0] * m
        lmax[0]  = height[0]
        rmax[-1] = height[-1]
        
        for i in range(1, m):
            lmax[i] = max(height[i], lmax[i-1])
        for i in range(m-2, -1, -1):
            rmax[i] = max(height[i], rmax[i+1])
        
        ans = 0
        for i in range(1, m-1):
            h = min(lmax[i-1], rmax[i+1])
            if h > height[i]:
                ans += h - height[i]
        return ans


