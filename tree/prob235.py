class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root.val == p.val or root.val == q.val:
            return root
              
        lb, ub = min(p.val, q.val), max(p.val, q.val)
        if root.val < lb:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > ub:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
