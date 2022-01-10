class MKAverage:

    def __init__(self, m: int, k: int):
        from sortedcontainers import SortedList
        from collections import deque
        
        self.m = m
        self.k = k
        self.sl = SortedList()
        self.q = deque()
        
    def addElement(self, num: int) -> None:
        
        self.sl.add(num)
        self.q.append(num)
        if len(self.sl) > self.m:
            element = self.q.popleft()
            self.sl.remove(element)
        

    def calculateMKAverage(self) -> int:
        
        if len(self.sl) < self.m:
            return -1
        
        return sum(self.sl[self.k:-self.k]) // (self.m - 2 * self.k)
            
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
