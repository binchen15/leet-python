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

User function Template for python3

# import sys
# sys.setrecursionlimit(3000)

from functools import lru_cache

class Solution:
    
    #Function to return the diameter of a Binary Tree.
    def diameter(self, root):
        # Code here
        if not root:
            return 0
        ans = [0]
        
        def walk(node):
            if not node:
                return
            if node.left:
                walk(node.left)
            if node.right:
                walk(node.right)
            ans[0] = max(ans[0], self.helper2(node))
        
        walk(root)
        return ans[0]
        
    @lru_cache(maxsize=None)
    def helper(self, node):
        # find the depth of a tree
        if not node:
            return 0
        return 1 + max(self.helper(node.left), self.helper(node.right))

    #@lru_cache(maxsize=None)
    def helper2(self, node):
        if not node:
            return 0
        return 1 + self.helper(node.left) + self.helper(node.right)
