class Trie(object):

    class Node(object):
        def __init__(self):
            self.children = {}  # map(char => Node)
            self.isLeaf   = False
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node() 

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        self._insert(word, self.root)
        
    def _insert(self, word, node):
        """internal method to be called by insert(),
           a recursive defintion """
        if not node:
            return
        if len(word) == 0:
            node.isLeaf = True
            return
        char = word[0]
        if char not in node.children:
            node.children[char] = self.Node()
        self._insert(word[1:], node.children[char])
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self._search(word, self.root)
        
    def _search(self, word, node):
        if not node:
            return False
        if len(word) == 0:
            return node.isLeaf
        char = word[0]
        if char not in node.children:
            return False
        return self._search(word[1:], node.children[char])
               

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self._startsWith(prefix, self.root)
    
    def _startsWith(self, prefix, node):
        if not node:
            return False
        if len(prefix) == 0:
            return True
        char = prefix[0]
        if char not in node.children:
            return False
        return self._startsWith(prefix[1:], node.children[char])
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
