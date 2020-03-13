# symmetric trees

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, s, t):
        """test if tree s and t are mirror reflections 
           to each other"""
        if not s and not t:
            return True
        if not s or not t:
            return False
        return  s.val == t.val and \
                self.isMirror(s.left, t.right) and \
                self.isMirror(s.right, t.left)
        


