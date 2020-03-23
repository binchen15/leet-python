# 1337	The K weakest rows in a matrix

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
    

# use heapq, not really faster. 38% solution
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])
        
        class Weakness(object):
            def __init__(self, i, c):
                self.i = i  # index
                self.c = c  # counts
            def __lt__(self, other):
                return self.c < other.c or \
                    (self.c == other.c and self.i < other.i)
                
        weakness = [ Weakness(i, self.count1s(n, row)) for i, row in enumerate(mat)]
        import heapq
        return list(map(lambda x: x.i, heapq.nsmallest(k, weakness)))
        
        
    def count1s(self, m, row):
        i = 0
        while i < m and row[i] == 1:
            i += 1
        return i
            
         
