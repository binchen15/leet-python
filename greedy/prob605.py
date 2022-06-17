# time limit error 66/124
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        m = len(flowerbed)
        
        def helper(bed, n):
            if n == 0:
                return True
            
            for i in range(m):
                if bed[i] == 0 and (i == 0 or bed[i-1] == 0) \
                    and (i == m-1 or bed[i+1] == 0):
                    bed[i] = 1
                    success = helper(bed, n-1)
                    if success:
                        return True
                    bed[i] = 0
            return False
        
        return helper(flowerbed, n)

# not any faster
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        m = len(flowerbed)
        avail = set(i for i, v in enumerate(flowerbed) if v == 0)


        def helper(bed, n, avail):
            if n == 0:
                return True

            for i in avail:
                if (i == 0 or bed[i-1] == 0) \
                    and (i == m-1 or bed[i+1] == 0):
                    bed[i] = 1
                    success = helper(bed, n-1, avail.difference({i}))
                    if success:
                        return True
                    bed[i] = 0
            return False

        return helper(flowerbed, n, avail)

# 84 cases passed. still nogood
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        m = len(flowerbed)
        avail = set(i for i, v in enumerate(flowerbed) if v == 0)

        bed = flowerbed

        @lru_cache(None)
        def helper(n, avail):
            if n == 0:
                return True

            for i in avail:
                if (i == 0 or bed[i-1] == 0) \
                    and (i == m-1 or bed[i+1] == 0):
                    bed[i] = 1
                    success = helper(n-1, tuple(set(avail).difference({i})))
                    if success:
                        return True
                    bed[i] = 0
            return False

        return helper(n, tuple(avail))
