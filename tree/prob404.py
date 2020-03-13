# 404 Sum of left leaf nodes

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0   #?
        if self.isLeaf(root.left):
            return root.left.val + \
                   self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left) + \
                    self.sumOfLeftLeaves(root.right)
        
        
    def isLeaf(self, node):
        return node and \
               not node.left and \
               not node.right
        
