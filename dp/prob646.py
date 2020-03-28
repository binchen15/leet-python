# 646 Maximum Length of Pair Chain

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        m = len(pairs)
        if m <= 1:
            return m
        # sort by begin of the pair
        pairs.sort(key=lambda x : x[0])
        
        # ML of chain ends at pairs[i]
        dp = [1] * m
        for i in range(1, m):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
