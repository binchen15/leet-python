class Solution:
    def divisorGame(self, n: int) -> bool:
        
        def findDivisor(n):
            # ans = -1
            # for i in range(n-1, 0, -1):
            for i in range(1, n):
                if n % i == 0:
                    return i
                
            return -1
        
        cnt = 0  # count of moves
        
        while True:
            d = findDivisor(n)
            if d != -1:
                n = n - d
                cnt += 1
            else:
                break
        
        return cnt % 2 == 1
