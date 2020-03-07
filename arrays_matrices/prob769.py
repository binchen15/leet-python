class Solution(object):
    """my most satisfactory one up to now. Mar. 7 2020 Sat. Morning
		idea. up to arr[i] the maxium so far must be equal to index i
        to guarantee a chunck 
	"""
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        np  = 0  # number of partitions
        rec = -1 # current max value
        i   = 0  # current index
        m   = len(arr)
        while i < m:
            rec = max(rec, arr[i])
            if rec == i:
                np += 1
            i += 1
        return np
