# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# diameter counts edges, not nodes
# height count nodes.
# two ends of the diameter might not both be leaves. 

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        
        dl = self.diameterOfBinaryTree(root.left)
        dr = self.diameterOfBinaryTree(root.right)
        d0 = self.height(root.left) + self.height(root.right)
        return max(dl, dr, d0)
        
        
    def height(self, root):
        if not root:
            return 0
        else:
            return 1 + max(
                self.height(root.left),
                self.height(root.right)
            )
        
