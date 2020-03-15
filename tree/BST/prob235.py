# 235 BST lowest common ancestor

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not p or not q:
            return None
        if root.val == p.val:
            return p
        if root.val == q.val:
            return q
        
        if p.val < root.val and \
           q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q) 
        elif p.val > root.val and \
            q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        


