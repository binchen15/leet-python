# 1385 distance value between two arrays

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        m = len(arr1)
        n = len(arr2)
        cnt = 0
        for a in arr1:
            flag = True
            for b in arr2:
                if abs(a-b) <= d:
                    flag = False
                    break
            if flag:
                cnt += 1
        return cnt
        
