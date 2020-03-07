class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i, v in enumerate(nums):
            if v not in d:
                d[v] = [1, i, i]
            else:
                d[v][0] += 1
                d[v][1] = min(d[v][1], i)
                d[v][2] = max(d[v][2], i)
                
        #deg  = max(map(lambda x: x[0], d.values())) 
        deg  = max(d[k][0] for k in d) 
        subs = filter(lambda x: x[0] == deg, d.values())
        
        lens = [ d[2] - d[1] for d in subs]
        return min(lens) + 1
    
        
