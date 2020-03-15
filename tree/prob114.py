# 114 flatten binary tree to linked list

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        if not root.left and not root.right:
            return
        if not root.left:
            self.flatten(root.right)
            return
        if not root.right:
            self.flatten(root.left)
            root.right = root.left
            root.left  = None
            return
        # both left and right not null
        self.flatten(root.left)
        self.flatten(root.right)
        curr = root.left
        while curr.right:
            curr = curr.right
        curr.right = root.right
        root.right = root.left
        root.left  = None

