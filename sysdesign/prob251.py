class Vector2D:

    def __init__(self, vec: List[List[int]]):
        #  self.vec2d = vec
        self.vec1d = [e for row in vec for e in row]
        self.size = len(self.vec1d)
        self.index = 0   # point to next element 

    def next(self) -> int:
        ans = self.vec1d[self.index]
        self.index += 1
        return ans

    def hasNext(self) -> bool:
        return self.index < self.size:wq
