# 922 Sort array by parity II

# double pointers 80% in speed
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        m  = len(A)
        ep = 0 # even index ptr
        op = 1 # odd. index ptr
        while ep < m-1 and op < m:
            while ep < m-1 and not (A[ep] & 1):
                ep += 2
            if ep >= m-1:
                break
            while op < m and (A[op] & 1):
                op += 2
            if op >= m:
                break
            tmp   = A[ep]
            A[ep] = A[op]
            A[op] = tmp
            op += 2
            ep += 2
        return A
        
