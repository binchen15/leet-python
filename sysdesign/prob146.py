class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.od = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        ans = self.od[key]
        self.od.move_to_end(key, last=True)
        return ans

    def put(self, key: int, value: int) -> None:
        self.od[key] = value
        self.od.move_to_end(key, last=True)
        if len(self.od) > self.capacity:
            self.od.popitem(last=False)
