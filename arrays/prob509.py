# 509 Fibonacci number

# recursion. 25% in speed
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        return self.fib(N-2) + self.fib(N-1)
       
# memoization 90%

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        memo = [0] * (N + 1)
        memo[1] = 1
        for i in range(2, N+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[N]
        
 
