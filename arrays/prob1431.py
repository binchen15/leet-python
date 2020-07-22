class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        m = len(candies)
        ans = [False] * m
        ub = max(candies)
        for i in range(m):
            if candies[i] + extraCandies >= ub:
                ans[i] = True
        return ans
        
