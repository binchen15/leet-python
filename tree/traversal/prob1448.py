class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.ans = 0 
        def walk(root, ub):
            if not root:
                return
            
            if ub <= root.val:
                self.ans += 1
            ub = max(ub, root.val)
            
            if root.left:
                walk(root.left, ub)
            if root.right:
                walk(root.right, ub)
                
        walk(root, root.val)
        
        return self.ans
