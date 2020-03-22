# 1299 Replace Elements with Greatest element on right side

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ub = max(arr)
        m  = len(arr)
        for i in range(m-1):
            if arr[i] == ub:  # update upper bound
                ub = max(arr[i+1:])
            arr[i] = ub
        arr[-1] = -1
        return arr
        
