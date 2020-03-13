#617. Merge two binary trees

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1

        t1.val  += t2.val  # combine the root value first
        # the merged output must be re-assigned...
        t1.left  = self.mergeTrees(t1.left,  t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
