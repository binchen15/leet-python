class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        
        cnts = 0
        
        while num1 and num2:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            cnts += 1
            
        return cnts
