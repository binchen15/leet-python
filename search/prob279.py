# 279 Perfect squares

# 50% dynamic programming solution.
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        # perfect square numbers allowed
        nums = [ i * i for i in range(1, int(math.sqrt(n)) + 1 )]
        dp = list(range(n+1)) # n = 1 + 1 + 1 + ... + 1. upper bound
        # dp[:4] is correct already
        for i in range(4, n+1):  # work on dp[i] using previous results
            for j in nums:
                if j <= i:
                    dp[i] = min(dp[i], 1 + dp[i-j])
                else:
                    break
        return dp[n]

# tree. search by level-order traversal  
# 82%
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        # perfect square numbers allowed
        nums = [ i * i for i in range(1, int(math.sqrt(n)) + 1 )]
        currL = [n]
        nextL = []
        cnt   = 0   # number of levels travelled so far
        while currL:
            cnt += 1
            while currL:
                i = currL.pop(0)
                for j in nums:
                    if j < i:
                        nextL.append(i-j)
                    elif j == i:  # found a solution
                        return cnt
                    else:  # j > i, quit inner loop
                        break
            currL = list(set(nextL)) # remove duplicates
            nextL = []


# tree. search by level-order traversal
# 90%
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        # perfect square numbers allowed
        nums = [ i * i for i in range(1, int(math.sqrt(n)) + 1 )]
        currL = [n]
        nextL = []
        cnt   = 0   # number of levels travelled so far
        marked    = [False] * (n+1)
        marked[n] = True
        while currL:
            cnt += 1
            while currL:
                i = currL.pop(0)
                for j in nums:
                    if j < i:
                        if not marked[i-j]:
                            nextL.append(i-j)
                            marked[i-j] = True
                    elif j == i:  # found a solution
                        return cnt
                    else:  # j > i, quit inner loop
                        break
            currL = nextL
            nextL = []

# BFS with visited set
class Solution:
    def numSquares(self, n: int) -> int:

        if n == 1:
            return 1

        nums = [i*i for i in range(1, int(math.sqrt(n))+1)]

        cur = [n]
        nxt = set()
        cnt = 1
        visited = set()

        while True:
            while cur:
                val = cur.pop(0)
                visited.add(val)
                for sq in nums:
                    if sq == val:
                        return cnt
                    elif sq < val:
                        remain = val - sq
                        if remain not in visited:
                            nxt.add(remain)
                    else:
                        break

            cur = list(nxt)
            nxt = set()
            cnt += 1

