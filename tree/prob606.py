class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        if not root:
            return ""
        
        pre = str(root.val)
        
        l, r = self.tree2str(root.left), self.tree2str(root.right)
        
        if not l and not r:
            return pre
        if not l:
            return f"{pre}()({r})"
        if not r:
            return f"{pre}({l})"
        
        return f"{pre}({l})({r})"
