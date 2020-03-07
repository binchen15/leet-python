class Solution(object):
    """this refereed to answers. I am not this smart"""
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ret = list(range(1, n + 1))
        # rearrange ret[0:k+1] create k distances
        i = 1  # starting index
        delta = k
        while i < k + 1:
            if i & 1:
                ret[i] = ret[i-1] + delta
            else:
                ret[i] = ret[i-1] - delta
            delta -= 1
            i += 1
        return ret
        
