# time limit
class Solution:
    def lastRemaining(self, n: int) -> int:

        cur = [ i for i in range(1, n+1) ]
        nxt = []
        forward = True

        while len(cur) > 1:
            if forward:
                i = 1
                while i < len(cur):
                    nxt.append(cur[i])
                    i += 2
            else:
                i = len(cur) - 1 - 1
                while i >= 0:
                    nxt.append(cur[i])
                    i -= 2
                nxt = nxt[::-1]
            forward = not forward
            cur = nxt
            nxt = []

        return cur[0]

