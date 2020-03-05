class Solution(object):
    "46%"
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
    
        bx = "{:032b}".format(x)
        by = "{:032b}".format(y)
        
        tot = 0
        for i in range(len(bx)):
            if bx[i] != by[i]:
                tot += 1
        return tot
        

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        z   = x ^ y  # xor operation
        tot = 0
        while z > 0:
            if z & 1 == 1:  # last bit
                tot += 1
            z =  z >> 1
        return tot


