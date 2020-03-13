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



