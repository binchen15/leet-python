# 896 Monotonic array

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        m = len(A)
        if m == 1:
            return True
        
        flag = A[1] - A[0]
        for i in range(2, m):
            if A[i] > A[i-1]:
                if flag < 0:
                    return False
                elif flag == 0:
                    flag = A[i] - A[i-1]
            elif A[i] < A[i-1]:
                if flag > 0:
                    return False
                elif flag == 0:
                    flag = A[i] - A[i-1]
        return True

# essentially same, slightly faster. 85%
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        m = len(A)
        if m == 1:
            return True        
        flag = A[1] - A[0]
        for i in range(2, m):
            if A[i] != A[i-1]:
                if flag == 0:
                    flag = A[i] - A[i-1]
                elif (A[i] - A[i-1]) * flag < 0:
                    return False
   
        return True

