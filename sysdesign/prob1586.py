class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.data = self.inOrder(root)
        self.size = len(self.data)
        self.index = -1

    def inOrder(self, root):
        if not root:
            return []
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)
        
    def hasNext(self) -> bool:
        return self.index + 1 < self.size

    def next(self) -> int:
        self.index += 1
        return self.data[self.index] 

    def hasPrev(self) -> bool:
        return self.index - 1 >= 0

    def prev(self) -> int:
        self.index -= 1
        return self.data[self.index]
        
