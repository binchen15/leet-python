# Subtract the Product and Sum of Digits of an Integer

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = map(int, list(str(n)))

        from functools import reduce
        prod = reduce(lambda x, y : x * y, digits)
        add  = reduce(lambda x, y : x + y, digits)
        return prod - add
