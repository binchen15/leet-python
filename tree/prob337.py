# 337 House Robber III

"""timeout error"""
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        # without robbing the root
        v1 = self.rob(root.left) + self.rob(root.right)
        
        # amount including the root 
        v2 = root.val
        if root.left:
            l = self.rob(root.left.left) + self.rob(root.left.right) 
        else:
            l = 0
        if root.right:
            r = self.rob(root.right.left) + self.rob(root.right.right)
        else:
            r = 0
        v2 += l + r
        
        return max(v1, v2)
        
# same as above, but with memoization
# 36% in performance
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if hasattr(root, "amount"):
            return root.amount

        # without robbing the root
        v1 = self.rob(root.left) + self.rob(root.right)

        # amount including the root
        v2 = root.val
        if root.left:
            l = self.rob(root.left.left) + self.rob(root.left.right)
        else:
            l = 0
        if root.right:
            r = self.rob(root.right.left) + self.rob(root.right.right)
        else:
            r = 0
        v2 += l + r

        root.amount = max(v1, v2)
        return root.amount


