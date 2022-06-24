class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        vals1, vals2 = [], []
        
        self.walk(root1, vals1)
        self.walk(root2, vals2)
        
        return vals1 == vals2
        
    def walk(self, root, vals):
        if not root:
            return 
        if not root.left and not root.right:
            vals.append(root.val)
            return
        if root.left:
            self.walk(root.left, vals)
        if root.right:
            self.walk(root.right, vals)
