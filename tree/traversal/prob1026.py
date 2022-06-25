class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        
        def walk(root, val):
            if root.left:
                walk(root.left, val)
            self.ans = max(self.ans, abs(val - root.val))
            if root.right:
                walk(root.right, val)
                
        def walk2(root):
            if root.left:
                walk2(root.left)
                
            walk(root, root.val)
                
            if root.right:
                walk2(root.right)
                
                
        walk2(root)
        return self.ans

# 94% solution
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        def dfs(root, lb, ub):
            if not root:
                return
            lb = min(lb, root.val)
            ub = max(ub, root.val)
            self.ans = max(self.ans, ub-lb)

            if root.left:
                dfs(root.left, lb, ub)
            if root.right:
                dfs(root.right, lb, ub)

        dfs(root, root.val, root.val)

        return self.ans
