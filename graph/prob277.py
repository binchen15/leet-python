# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        for i in range(n):
            if self.everybody_knows_me(n, i) and self.i_knows_nobody(n, i):
                return i
        return -1
        
        
        
    def everybody_knows_me(self, n, i):
        for j in range(n):
            if not knows(j, i):
                return False
        return True
    
    def i_knows_nobody(self, n, i):
        for j in range(n):
            if i == j:
                continue
            if knows(i, j):
                return False
        return True
