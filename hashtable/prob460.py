from collections import defaultdict

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def insertFront(self, node):
        "insert at the beginning"
        self.size += 1
        tmp = self.head.next
        self.head.next = node
        node.next = tmp
        node.prev = self.head
        tmp.prev = node
        
    def popLast(self):
        "pop the last element"
        if self.size == 0: 
            return None
        self.size -= 1
        node = self.tail.prev
        prev = node.prev
        prev.next = self.tail
        self.tail.prev = prev
        return node
        
    
    def removeNode(self, node):
        "remove a given node"
        if self.size == 0:
            return None
        prv = node.prev
        nxt = node.next
        prv.next = nxt
        nxt.prev = prv
        self.size -= 1
    
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.freq = defaultdict(DList)
        self.min_freq = 0
        
    def touch(self, key):
        "update the key frequency by 1"
        node = self.cache[key]
        freq = node.freq
        dlist = self.freq[freq]
        dlist.removeNode(node)
        if freq == self.min_freq and dlist.size == 0:
            self.min_freq += 1            
        node.freq += 1
        self.freq[node.freq].insertFront(node)
        
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.touch(key)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if self.capacity == 0:
            return
        
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.touch(key)
        else:
            if self.size == self.capacity:
                dlist = self.freq[self.min_freq]
                node = dlist.popLast()
                self.size -= 1
                self.cache.pop(node.key)
            newNode = Node(key, value)
            self.cache[key] = newNode
            self.min_freq = 1
            self.size += 1
            self.freq[1].insertFront(newNode)
            
                
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

