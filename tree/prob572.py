# 572 subtree

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s:
            return False
        if not t:
            return True

        if self.sameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or \
               self.isSubtree(s.right, t)


    def sameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and \
               self.sameTree(s.left, t.left) and \
               self.sameTree(s.right, t.right)


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if self.isCopy(root, subRoot):
            return True
        
        if root.left and self.isSubtree(root.left, subRoot):
            return True
        
        if root.right and self.isSubtree(root.right, subRoot):
            return True
        
        return False
        
    def isCopy(self, root1, root2):
        
        if not root1 and not root2:
            return True
        
        if not root1 or not root2:
            return False
        
        if root1.val != root2.val:
            return False
        
        return self.isCopy(root1.left, root2.left) and self.isCopy(root1.right, root2.right)
