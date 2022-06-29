# timelimit error. 8 cases passed
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        m = len(heights)
        n = len(heights[0])
        
        def findNext(i,j):
            l = ((i+1,j), (i-1,j), (i,j+1), (i,j-1))
            l = [ (i,j) for (i,j) in l if 0 <= i < m and 0 <= j < n]
            return l
        
        self.minEffort = sys.maxsize
        
        def walk(path, effort, i, j):
            if path:
                i0, j0 = path[-1]
                tmp = abs(heights[i][j] - heights[i0][j0])
                effort = max(effort, tmp)
            if effort > self.minEffort:
                return
            if (i, j) == (m-1, n-1):
                if effort < self.minEffort:
                    self.minEffort = effort
                return
            
            nxts = findNext(i, j)
            nxts = [p for p in nxts if p not in path]
            if not nxts:
                return
            
            for nxt in nxts:
                walk(path+[(i,j)], effort, *nxt)
                
        walk([], 0, 0, 0)
                
        return self.minEffort

