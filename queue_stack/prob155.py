class MinStack(object):
    """the self.min_stack records the history of min values.."""

    def __init__(self):
        """
        initialize your data structure here.
        """
        import sys
        self.data_stack = []
        self.min_stack  = []
        self.min =  sys.maxsize
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.min = min(self.min, x)
        self.data_stack.append(x)
        self.min_stack.append(self.min)

    def pop(self):
        """
        :rtype: None
        """
        del self.data_stack[-1]  
        del self.min_stack[-1]
        if self.min_stack:
            self.min = self.min_stack[-1]
        else:
            import sys
            self.min = sys.maxsize

    def top(self):
        """
        :rtype: int
        """
        return self.data_stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
