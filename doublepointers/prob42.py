# prob 42 trap rain water
# two pointer solution
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n <= 2:
            return 0

        res = 0
        lMax = 0
        rMax = 0
        l = 0
        r = n - 1

        while l <= r:
            if lMax >= rMax:
                res += max(rMax-height[r], 0)
                rMax = max(rMax, height[r])
                r -= 1
            else:
                res += max(lMax-height[l], 0)
                lMax = max(lMax, height[l])
                l += 1

        return res

