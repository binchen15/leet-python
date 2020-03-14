class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        d = {j:0 for j in J}
        for s in S:
            if s in d:
                d[s] += 1
        return sum(d.values())
        
