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
