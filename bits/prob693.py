class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bits = bin(n)[2:]
        if len(bits) == 1:
            return True
        for i in range(len(bits)-1):
            if bits[i+1] == bits[i]:
                return False
            else:
                i += 1
        return True
        
        
