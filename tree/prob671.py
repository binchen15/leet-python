# 671. Find second minum of a special binary tree

# 70% performance
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        if not root.left: # which means not root.right too
            return -1

        # root has two children
        if root.left.val < root.right.val:
            l = self.findSecondMinimumValue(root.left)
            if l == -1:
                return root.right.val
            else:
                return min(l, root.right.val)
        elif root.left.val > root.right.val:
            r = self.findSecondMinimumValue(root.right)
            if r == -1:
                return root.left.val
            else:
                return min(root.left.val, r)
        else:
            l = self.findSecondMinimumValue(root.left)
            r = self.findSecondMinimumValue(root.right)
            if l == -1 and r == -1:
                return -1
            elif l == -1:
                return r
            elif r == -1:
                return l
            else:
                return min(l, r)

