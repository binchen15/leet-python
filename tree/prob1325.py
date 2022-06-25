class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        if root.val == target and self.isLeaf(root):
            return None
        
        root.left = self.removeLeafNodes(root.left, target)        
        root.right = self.removeLeafNodes(root.right, target)
        
        if root.val != target:
            return root
        if self.isLeaf(root):
            return None
        return root
        
        
    def isLeaf(self, node):
        """is a node a leaft node?"""
        return node and not node.left and not node.right 
