class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1 = {}
        d2 = {}
        
        for n in nums1:
            d1[n] = d1.get(n,0) + 1
            
        for n in nums2:
            d2[n] = d2.get(n,0) + 1
            
        d = {}
        for n in d1:
            if n in d2:
                d[n] = min(d1[n], d2[n])
                
        ret = []
        for n in d:
            for _ in range(d[n]):
                ret.append(n)
        return ret
        
