# UNIVALUED Binary Tree

# recursion
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root.left and not root.right:
            return True
        if not root.left:
            return self.isUnivalTree(root.right) and \
                root.val == root.right.val
        if not root.right:
            return self.isUnivalTree(root.left) and \
                root.val == root.left.val
        return  self.isUnivalTree(root.right) and \
                self.isUnivalTree(root.left) and \
                root.val == root.left.val and \
                root.val == root.right.val
       
