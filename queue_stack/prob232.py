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
        
# this realy did what the problem asked for
# using two stacks. 
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_push = []
        self.stack_pop  = []
        
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack_push.insert(0, x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.stack_pop:
            x = self.stack_pop[0]
            del self.stack_pop[0]
            return x
        else:  # transfer data from push stack to pop stack
            self.transfer()
            return self.pop()    
            
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack_pop:
            return self.stack_pop[0]
        else:  # transfer data from push stack to pop stack
            self.transfer()
            return self.peek()    

    def transfer(self):
        for _ in range(len(self.stack_push)):
            x = self.stack_push[0]
            self.stack_pop.insert(0, x)
            del self.stack_push[0]
        
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack_push) + len(self.stack_pop) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

