# 728 Self Dividing Numbers

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = [ n  for n in range(left, right+1) if self.test(n)]
        return ans

    def test(self, n):
        """if n is self divisible"""
        for c in str(n):
            d = int(c)
            if d == 0:
                return False
            elif n % d:
                return False
        return True

