# 1051 Height Checker

# used map.

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        hc = {}
        for h in heights:
            hc[h] = hc.get(h, 0) + 1
        
        hp = sorted(hc.items(), key=lambda x: x[0])
        ladders = [ [ hp[0][0], 0, hp[0][1]-1 ]  ] # height, start, end
        for i in range(1, len(hp)):
            row = [ hp[i][0], ladders[i-1][2]+1, ladders[i-1][2]+hp[i][1] ]
            ladders.append(row)
        lmap = { row[0]: (row[1], row[2]) for row in ladders }

        cnt = 0
        for i, hgt in enumerate(heights):
            bnds = lmap[hgt] # [min, max] index
            if i < bnds[0] or i > bnds[1]:
                cnt += 1
        return cnt
    
    
