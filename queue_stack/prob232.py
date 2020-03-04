# implement queue via stack operations
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        x = self.data[0]
        del self.data[0]
        return x
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.data[0]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.data) == 0
        
