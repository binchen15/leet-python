class Solution(object):
    """40%"""
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        data= sorted(d.items(), 
                     key= lambda x : x[1], reverse=True)
        return data[0][0]

class Solution(object):
    """70%"""
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        rec = max(d.values())
        for k in d:
            if d[k] == rec:
                return k
