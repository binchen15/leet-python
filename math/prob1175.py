class Solution:
    def numPrimeArrangements(self, n: int) -> int:
    
        if n == 1:
            return 1
        
        cnts = 0
        for i in range(2, n+1):
            if self.isPrime(i):
                cnts += 1
                
        return factorial(n-cnts)*factorial(cnts) % (10**9 + 7)
            
    def factorial(self, n):
        if n == 1:
            return 1
        return n*self.factorial(n-1)
        
    def isPrime(self, n):
        if n == 1:
            return False
        
        for i in range(2, n):
            if n % i == 0:
                return False
            
        return True

# slightly faster
class Solution:
    def numPrimeArrangements(self, n: int) -> int:

        if n == 1:
            return 1

        cnts = 0
        for i in range(2, n+1):
            if self.isPrime(i):
                cnts += 1

        return factorial(n-cnts)*factorial(cnts) % (10**9 + 7)

    def factorial(self, n):
        ans = 1
        for i in range(2, n+1):
            ans *= i
        return ans


    def isPrime(self, n):
        if n == 1:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False

        return True
