class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.data = self.inOrder(root)
        self.size = len(self.data)
        self.index = 0
        
    def inOrder(self, root):
        if not root:
            return []
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)
        
    def next(self) -> int:
        ans = self.data[self.index]
        self.index += 1
        return ans

    def hasNext(self) -> bool:
        return self.index < self.size
