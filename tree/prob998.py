class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        
        if root.val < val:
            head = TreeNode(val)
            head.left = root
            return head
        
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
