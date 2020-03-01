class Solution(object):
    """flower bed"""
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # n <= m
        m = len(flowerbed)
        if n == 0:
            return True
        if m == 0:
            return True
        
        i = 0      # current spot
        counts = 0 # total planted
        while i < m:
            if flowerbed[i] == 1:
                i += 1
                continue
            else: #  candidate
                if i == 0 or flowerbed[i-1] == 0:
                    front = True
                else:
                    front = False
                if i == m - 1 or flowerbed[i+1] == 0:
                    end = True
                else:
                    end = False
                if front and end:
                    flowerbed[i] = 1
                    counts += 1
                i += 1
            if counts == n:
                break
        if counts == n:
            return True
        else:
            return False
        
        
