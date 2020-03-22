# 1304 find N unique inteters sum up to zero

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n & 1:
            avg = (n+1) // 2
            ans = [ i - avg  for i in range(1, n+1)]
        else:
            ub = n // 2
            ans = [ i for i in range(1, ub+1)] + [ -i for i in range(1, ub+1)]
        return ans
        
