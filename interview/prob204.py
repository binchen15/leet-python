# 204 Count prime

# this times out....
class Solution(object):
    import math
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: 
            return 0
        cnt = 0
        for i in range(2, n): # less than n
            if self.isPrime(i):
                cnt += 1
        return cnt
        
    def isPrime(self, n):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        
        ub = int(math.sqrt(n))
        for i in range(2, ub + 1):
            if n % i == 0:
                return False
        return True

# 5% solution... but accepted..
class Solution(object):
    import math
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: 
            return 0
        
        memo = [2,]
        
        for i in range(3, n): # less than n
            if self.isPrime(i, memo):
                memo.append(i)
        return len(memo)
        
    def isPrime(self, n, memo):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        ub = int(math.sqrt(n))
        for p in memo:
            if p > ub:
                return True
            elif n % p == 0:
                return False
        return True

# thieves of Eratosthenes 10%....
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        if n <= 2: 
            return 0
        bools = [1] * n  # assume 0 to n-1 are all primes
        bools[0] = 0
        bools[1] = 0
        for i in range(2, int(math.sqrt(n))+1):
            j = 2
            while i*j < n:
                bools[i*j] = 0
                j += 1
        return sum(bools)
