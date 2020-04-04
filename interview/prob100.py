# 100 Same (Binary) Tree

# based on recursion
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if  (p and not q) or \
            (q and not p):
            return False
        if not p and not q:
            return True
        return (p.val == q.val) and \
            self.isSameTree(p.left,  q.left) and \
            self.isSameTree(p.right, q.right)
    
    
