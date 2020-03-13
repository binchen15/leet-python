class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l = self.longestUnivaluePath(root.left)
        r = self.longestUnivaluePath(root.right)
        if root.left and root.val == root.left.val:
            cl = 1 + self.longestPathFromRoot(root.left)
        else:
            cl = 0
        if root.right and root.val == root.right.val:
            cr = 1 + self.longestPathFromRoot(root.right)
        else:
            cr = 0
        if cl and cr:
            c = cl + cr
        else:
            c = max(cl, cr)
        return max(l,r,c)
        
        
    def longestPathFromRoot(self, root):
        """longest unique value path from the root downward"""
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        if not root.left:
            if root.val == root.right.val:
                return 1 + self.longestPathFromRoot(root.right)
            else:
                return 0
        if not root.right:
            if root.val == root.left.val:
                return 1 + self.longestPathFromRoot(root.left)
            else:
                return 0
        # both children exist
        if root.val == root.right.val:
            right =  1 + self.longestPathFromRoot(root.right)
        else:
            right = 0
        if root.val == root.left.val:
            left =  1 + self.longestPathFromRoot(root.left)
        else:
            left = 0
        return max(left, right)
                

