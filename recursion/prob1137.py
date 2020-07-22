# tribonacci number

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        tribo = [0, 1, 1]
        if n <= 2:
            return tribo[n]
        for i in range(3, n+1):
            new = tribo[-1] + tribo[-2] + tribo[-3]
            tribo.append(new)

        return tribo[-1]
