# 1122 Relative sort array

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        wc = {}
        for n in arr1:
            wc[n] = wc.get(n, 0) + 1
        ans = []
        for n in arr2:  # relative order in arr2 kept
            ans.extend([n]*wc[n])
            del wc[n]
        for n in sorted(wc.keys()): # tail sorted too
            ans.extend([n]*wc[n])
        return ans

