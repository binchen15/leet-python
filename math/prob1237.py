# 5% solution

class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        ans = []
        y_max = 1000
        for x in range(1, 1001):
            y = 1
            while y <= y_max:
                if customfunction.f(x,y) == z:
                    ans.append([x,y])
                    y_max = y - 1
                    break
                else:
                    y += 1
        return ans
    
# 25% solution
class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        ans  = []
        l, h = 1, 1000
        for x in range(1, 1001):
            y = self.bisect(z, customfunction.f, x, l, h)
            if y >= 0:
                ans.append([x, y])
                h = y - 1
        return ans
    
    def bisect(self, z, f, x, l, h):
        if f(x, h) < z or f(x, l) > z:
            return -1
        while l <= h:
            mid = l + (h-l)//2
            v = f(x, mid)
            if v == z:
                return mid
            elif v > z:
                h = mid - 1
            else:
                l = mid + 1
        return -1  # not found
            
