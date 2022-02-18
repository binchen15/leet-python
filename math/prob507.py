class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        if num <= 2:
            return False
        
        s = 1
        
        ub = int(math.sqrt(num))
        
        for i in range(2, ub+1):
            if num % i == 0:
                s += i + num // i
                if s > num:
                    return False
                
        return s == num
