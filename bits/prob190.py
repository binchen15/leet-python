class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bits = []
        for _ in range(32):
            bit = n % 2
            bits.append(bit)
            n >>= 1
        ans = 0
        for bit in bits:
            ans = ans*2 + bit
        return ans

class Solution:
    def reverseBits(self, n):
        bits = []
        for _ in range(32):
            bit = n & 1
            bits.append(bit)
            n >>= 1
        ans = 0
        for bit in bits:
            ans = (ans << 1) + bit
        return ans

