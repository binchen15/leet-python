class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.lb = self.findMin(self.root)
        self.ub = self.findMax(self.root)
        self.cur = -1
        
    def findMin(self, root):
        if not root:
            return None
        cur = root
        while cur.left:
            cur = cur.left
         
        return cur.val
    
    def findMax(self, root):
        if not root:
            return None
        cur = root
        while cur.right:
            cur = cur.right
            
        return cur.val
      
        
    def findNext(self, root):
        
        # print(self.cur, root)
        if self.cur < self.lb:
            self.cur = self.lb
            return self.lb
        
        if root.val <= self.cur:
            return self.findNext(root.right)
        if not root.left:
            self.cur = root.val
            return root.val
        max_l = self.findMax(root.left)
        if max_l == self.cur:
            self.cur = root.val
            return root.val
        else:
            return self.findNext(root.left)

    def next(self) -> int:    
        return self.findNext(self.root)
        
    def hasNext(self) -> bool:
        return self.cur < self.ub
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
