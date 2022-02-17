class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        
        memo = [0] * (n+1)
        memo[1], memo[2] = 1, 1
    
        for j in range(3, n+1):
            memo[j] = memo[j-1] + memo[j-2] + memo[j-3]
            
        return memo[n]

class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        
        a, b, c = 0, 1, 1
        
        for i in range(n-2):
            c, b, a = a + b + c, c, b
            
        return c
