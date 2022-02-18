class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        i = 1
        
        while True:
            tmp = i * i
            if tmp == num:
                return True
            elif tmp > num:
                return False
            else:
                i += 1
