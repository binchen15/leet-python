class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        if root.val == 0 and self.isLeaf(root):
            return None
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 1:
            return root
        if self.isLeaf(root):
            return None
        
        return root
            
        
    def isLeaf(self, node):
        return node and not node.left and not node.right
        
