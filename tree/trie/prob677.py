# 677 Map Sum pairs using trie

class MapSum(object):

    class Node(object):
        def __init__(self):
            self.children = {}
            self.val      = 0
            #self.isLeaf   = False 
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self._insert(key, val, self.root)
        
    def _insert(self, key, val, node):
        if not node:
            return 
        if len(key) == 0:
            node.val = val
            #node.isLeaf = True
            return
        char = key[0]
        if char not in node.children:
            node.children[char] = self.Node()
        self._insert(key[1:], val, node.children[char])
        
        
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self._sum(prefix, self.root)
        
        
    def _sum(self, prefix, node):
        if not node:
            return 0
        if len(prefix) == 0:
            return self._sum2(node)
        else:
            char = prefix[0]
            if char not in node.children:
                return 0
            else:
                return self._sum(prefix[1:], node.children[char])
        

    def _sum2(self, node):
        """collect/sum all node.val starting from given node"""
        if not node:
            return 0
        tot = node.val
        for char in node.children:
            tot += self._sum2(node.children[char])
        return tot
        
        
        
        
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


