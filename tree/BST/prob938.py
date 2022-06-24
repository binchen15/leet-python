# Range sum of BST

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        if L <= root.val <= R:
            return root.val + \
            self.rangeSumBST(root.left, L, R) + \
            self.rangeSumBST(root.right, L, R)
        elif root.val < L:
            return self.rangeSumBST(root.right, L, R)
        else:
            return self.rangeSumBST(root.left, L, R)

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        if not root:
            return 0
        
        val = root.val
        if val > high:
            return self.rangeSumBST(root.left, low, high)
        elif val == high:
            return val + self.rangeSumBST(root.left, low, high)
        elif val == low:
            return val + self.rangeSumBST(root.right, low, high)
        elif val < low:
            return self.rangeSumBST(root.right, low, high)
        else:
            return val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

