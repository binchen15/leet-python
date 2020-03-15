# 236. Lowest common ancestor

# a. this times out
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not p or not q:
            return None
        if root == p or root == q:
            return root
        # both on left, both on right, or one on each side
        if self.contains(root.left, p) and \
           self.contains(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        if self.contains(root.right, p) and \
           self.contains(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        return root
        
    def contains(self, root, node):
        """does tree root contains node? """
        if not root or not node:
            return False
        if root == node:
            return True
        return  self.contains(root.left, node) or \
                self.contains(root.right, node)
        
# b. still timeout
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not p or not q:
            return None
        if root == p or root == q:
            return root
        # both on left, both on right, or one on each side
        p1 = self.path(root, p)
        p2 = self.path(root, q)
        i  = 0  # start from root 
        m  = min(len(p1), len(p2))
        while i+1 < m and p1[i+1] == p2[i+1]:
            i += 1
        return p1[i]
            
        
    def contains(self, root, node):
        """does tree root contains node? """
        if not root or not node:
            return False
        if root == node:
            return True
        return  self.contains(root.left, node) or \
                self.contains(root.right, node)
        
    def path(self, root, node):
        """assume root contains node"""
        if root == node:
            return [root]
        elif self.contains(root.left, node):
            return [root] + self.path(root.left, node)
        else:
            return [root] + self.path(root.right, node)

# a2. this works... hmm. strange
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not p or not q:
            return None
        if root == p or root == q:
            return root
        
        if not root.left:
            return self.lowestCommonAncestor(root.right, p, q)
        if not root.right:
            return self.lowestCommonAncestor(root.left, p, q)
            
        # both on left, both on right, or one on each side
        if self.contains(root.left, p) and \
           self.contains(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        if self.contains(root.right, p) and \
           self.contains(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        return root
        
    def contains(self, root, node):
        """does tree root contains node? """
        if not root:
            return False
        if root == node:
            return True
        return  self.contains(root.left, node) or \
                self.contains(root.right, node)

