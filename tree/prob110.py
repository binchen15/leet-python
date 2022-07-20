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

# better solution
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        h = self.heightBalanced(root)
        return h != -1

    def heightBalanced(self, node):
        """return -1 if not balanced, and return height if balanced"""
        if not node:
            return 0

        l, r = self.heightBalanced(node.left), self.heightBalanced(node.right)
        if l == -1 or r == -1:
            return -1
        if abs(l-r) > 1:
            return -1
        return 1 + max(l, r)

from functools import lru_cache

#Function to check whether a binary tree is balanced or not.
class Solution:
    
    def isBalanced(self,root):
    
        #add code here
        if not root:
            return True
        
        def walk(node):
            if not node:
                return True
            if node.left:
                if not walk(node.left):
                    return False
            if node.right:
                if not walk(node.right):
                    return False
            return abs(self.helper(node.left) - self.helper(node.right)) <= 1
            
        return walk(root)
                
        
    @lru_cache(maxsize=None)
    def helper(self, node):
        if not node:
            return 0
        return 1 + max(self.helper(node.left), self.helper(node.right))
