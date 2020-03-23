# 985 Sum of even numbers after queries

class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        se = 0
        for n in A:
            if not (n & 1):
                se += n
        ans = []
        for q in queries:
            val = q[0]
            ind = q[1]
            t   = A[ind] + val # new val
            if A[ind] & 1: # was odd
                if t & 1:
                    pass
                else:
                    se += t
            else:  # was even
                if t & 1:  # now odd
                    se -= A[ind]
                else: # still even
                    se += val
            A[ind] = t
            ans.append(se)
        return ans
                   
