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

class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        a1 = [0] * n
        a2 = [0] * n
        
        for i in range(1, n):
            a1[i] = max(height[i-1], a1[i-1])
            
        for i in range(n-2, -1, -1):
            a2[i] = max(height[i+1], a2[i+1])
             
        ans = 0
        
        for i in range(n):
            bar = min(a1[i], a2[i])
            water = max(0, bar - height[i])
            ans += water
            
        return ans
