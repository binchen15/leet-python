# 279 Perfect Squares
import math

# time limit error
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = list(range(n+1)) # upper bound
        dp[1] = 1
        for i in range(2,n+1):
            s = int(math.sqrt(i))
            if s * s == i:
                dp[i] = 1
            else:
                for op1 in range(1, i//2+1):
                    op2 = i - op1
                    dp[i] = min(dp[i], dp[op1]+dp[op2])
        return dp[n]

# 35% solution
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        ub  = int(math.sqrt(n))
        sqns = [ i*i for i in range(1, ub+1)] 
        
        dp = list(range(n+1)) # upper bound
        dp[1] = 1
        for i in range(2, n+1):
            for sqn in sqns:
                if sqn == i:
                    dp[i] = 1
                    break
                if sqn > i:
                    break
                r = i - sqn
                dp[i] = min(dp[i], 1 + dp[r])
        return dp[n]


if __name__ == "__main__":
	s = Solution()
	print(s.numSquares(7691))

#---- time error
class Solution:
    def numSquares(self, n: int) -> int:

        if n == 1:
            return 1

        ub = int(math.sqrt(n))

        dp = [ [0] * (n+1) for _ in range(ub) ]
        for j in range(1, n+1):
            dp[0][j] = j

        for i in range(1, ub):
            val = (i+1)*(i+1)
            for j in range(1, n+1):
                if j < val:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-val])

        return dp[ub-1][n]

# 2D to 1D DP . 30% solution
class Solution:
    def numSquares(self, n: int) -> int:

        if n == 1:
            return 1

        ub = int(math.sqrt(n))

        dp = [0] * (n+1)
        for j in range(1, n+1):
            dp[j] = j

        for i in range(1, ub):
            val = (i+1)*(i+1)
            for j in range(val, n+1):
                    dp[j] = min(dp[j], 1 + dp[j-val])

        return dp[n]
