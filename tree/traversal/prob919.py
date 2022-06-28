class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        
    def insert(self, val: int) -> int:
        if not self.root:
            self.root = TreeNode(val)
            return None
        
        cur = [self.root]
        nxt = []
        
        while True:
            while cur:
                node = cur.pop(0)
                if not node.left:
                    node.left = TreeNode(val)
                    return node.val
                else:
                    nxt.append(node.left)
                    
                if not node.right:
                    node.right = TreeNode(val)
                    return node.val
                else:
                    nxt.append(node.right)
                    
            if nxt:
                cur = nxt
                nxt = []
            else:
                break
                    

    def get_root(self) -> Optional[TreeNode]:
        return self.root
