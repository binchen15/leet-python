# 1217 play with chips

class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        ec = 0
        oc = 0
        for chip in chips:
            if chip & 1:
                oc += 1
            else:
                ec += 1
        return min(oc, ec)
