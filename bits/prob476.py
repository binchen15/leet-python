class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bits = map(int, list(bin(num)[2:]))
        m    = len(bits)
        ones = [1] * m
        flipped = [ bits[i] ^ ones[i] for i in range(m) ]
        ans = 0
        for bit in flipped:
            ans = (ans << 1) + bit
        return ans
        

