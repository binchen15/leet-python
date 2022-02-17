# Binary Gap

class Solution:
    def binaryGap(self, n: int) -> int:

        s = bin(n)[2:]
        if s.count("1") <= 1:
            return 0

        stk = []
        ans = 0
        n = len(s)

        for i in range(n):
            if s[i] == "1":
                if not stk:
                    stk.append(i)
                else:
                    d = i - stk[0]
                    if d > ans:
                        ans = d
                    stk[0] = i

        return ans
