class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return root
        
        if root.right:
            right = self.increasingBST(root.right)
            root.right = right
        
        if root.left:
            tail = self.findTail(root.left)
            left = self.increasingBST(root.left)
            tail.right = root
            root.left = None  # critical
            return left
        else:
            return root
        
    def findTail(self, root):
        if not root:
            return root
        cur = root
        while cur.right != None:
            cur = cur.right
        return cur
        
