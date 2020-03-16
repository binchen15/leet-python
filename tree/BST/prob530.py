# 530. Minimum absolute difference in BST


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        vals = []
        self.inorder(root, vals)
        ans = vals[-1] - vals[0]
        m   = len(vals)
        for i in range(m-1):
            d = vals[i+1] - vals[i]
            if d < ans:
                ans = d
        return ans
        
        
    def inorder(self, root, vals):
        if not root:
            return
        if root.left:
            self.inorder(root.left, vals)
        vals.append(root.val)
        if root.right:
            self.inorder(root.right, vals)
        
