class Solution(object):
    """timeout"""
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        ans = 0
        #keys = sorted(d.keys())
        keys = d.keys()
        for k in keys:
            if k + 1 in keys:
                l = d[k] + d[k+1]
                if l > ans:
                    ans = l
            if k - 1 in keys:
                l = d[k] + d[k-1]
                if l > ans:
                    ans = l
        return ans
                
class Solution(object):
    """70%"""
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        d2 = {}
        for k in d.keys():
            if (k-1 not in d) and (k+1 not in d):
                continue
            else:
                d2[k] = d[k] + max(d.get(k-1,0), d.get(k+1,0))
                
        if d2:
            return max(d2.values())
        else:
            return 0        
