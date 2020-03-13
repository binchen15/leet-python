# 110 Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        hl = self.height(root.left)
        hr = self.height(root.right)
        if abs(hl - hr) <= 1 and \
            self.isBalanced(root.left) and \
            self.isBalanced(root.right):
            return True
        else:
            return False

    def height(self, root):
        if not root:
            return 0
        return 1 + max(
            self.height(root.left),
            self.height(root.right)
        )
