# prob. 437 Path sum III

# number of paths sum to a given value
# path does not have to start from root, or end at leaf.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0

        c0 = self.counts(root, sum)
        cl = self.pathSum(root.left,  sum)
        cr = self.pathSum(root.right, sum)
        return c0 + cl + cr
        
        
    def counts(self, root, num):
        # number of paths sum to num, but must start from root
        if not root:
            return 0
        
        if root.val == num:
            cnt = 1
        else:
            cnt = 0
    
        cl   = self.counts(root.left,  num - root.val)
        cr   = self.counts(root.right, num - root.val)
        cnt += cl + cr
        return cnt
    
