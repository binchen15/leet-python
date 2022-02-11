class MaxStack:

    def __init__(self):
        self.data = []
        
    def push(self, x: int) -> None:
        self.data.insert(0, x)

    def pop(self) -> int:
        return self.data.pop(0)
        
    def top(self) -> int:
        return self.data[0]

    def peekMax(self) -> int:
        return max(self.data)

    def popMax(self) -> int:
        v = max(self.data)
        self.data.remove(v)
        return v
