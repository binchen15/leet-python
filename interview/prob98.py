# 98 validate binary search tree

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        if root.left:
            if not self.isValidBST(root.left):
                return False
            max_l = self.maxBST(root.left)
            if max_l >= root.val:
                return False
            
        if root.right:
            if not self.isValidBST(root.right):
                return False
            min_r = self.minBST(root.right)
            if min_r <= root.val:
                return False
            
        return True
                
    def minBST(self, root):
        """find min value of a BST, assume root not-None"""
        curr = root
        while curr.left:
            curr = curr.left
        return curr.val
    
    def maxBST(self, root):
        """find max value of a BST, assume root not-None"""
        curr = root
        while curr.right:
            curr = curr.right
        return curr.val
    
