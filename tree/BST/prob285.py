class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        if not root or not p:
            return None
        
        if root.val < p.val:
            return self.inorderSuccessor(root.right, p)
        elif root.val == p.val:
            if not root.right:
                return None
            else:
                return self.findMin(root.right)
        else:
            tmp = self.inorderSuccessor(root.left, p)
            if tmp:
                return tmp
            else:
                return root
            
            
    def findMin(self, root):
        cur = root
        while cur.left:
            cur = cur.left
        return cur

