# 190 Reverse bits

class Solution:
    def reverseBits(self, n: int) -> int:
        #s = f"{n:032b}"
        s = bin(n)[2:].rjust(32, "0")
        r = s[::-1]
        return int(r, 2)
