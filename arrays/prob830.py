# 830 Positions of Large groups

class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ans = []
        m = len(S)
        start = 0
        end = 0
        while start < m:
            while end+1 < m and S[end+1] == S[start]:
                end += 1
            if end-start+1 >= 3:
                ans.append([start, end])
            start = end + 1
            end = start
        return ans

