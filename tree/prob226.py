# invert a binary tree

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        left = root.left
        root.left  = root.right
        root.right = left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
