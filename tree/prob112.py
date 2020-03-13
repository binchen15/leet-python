# prob. 112 Path sum

# sum of node values along a radius equals to the sum

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:   # not sure
            return False

        if not root.left and not root.right:
            if root.val == sum:
                return True
            else:
                return False

        if not root.left:
            if self.hasPathSum(root.right, sum-root.val):
                return True
            else:
                return False

        if not root.right:
            if self.hasPathSum(root.left, sum-root.val):
                return True
            else:
                return False

        # both root.left, and root.right exist
        if self.hasPathSum(root.left, sum-root.val) or \
            self.hasPathSum(root.right, sum-root.val):
            return True
        else:
            return False


