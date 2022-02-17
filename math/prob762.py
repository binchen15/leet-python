class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        def setBits(n):
            cnts = 0
            while n > 0:
                n, r = divmod(n, 2)
                if r:
                    cnts += 1
            return cnts
        
        def isPrime(n):
            if n == 1:
                return False
            for d in range(2, n):
                if n % d == 0:
                    return False
            return True
        
        ans = 0
        for n in range(left, right+1):
            if isPrime(setBits(n)):
                ans += 1
                
        return ans
