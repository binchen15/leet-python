class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if x == 0.0:
            return 0
        
        if n < 0:
            return 1.0/self.myPow(x, -n)
        
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == 2:
            return x*x
        
        q = n // 2
        r = n % 2
        res = self.myPow(x, q)
        if r:
            return res*res*x
        else:
            return res*res
        
