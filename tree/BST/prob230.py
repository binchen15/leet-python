# prob. 230 Kthsmallest element Medium

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        data = []
        self.inorder(root, data)
        return data[k-1]
        
    def inorder(self, root, ans):
        # inorder traversal
        if not root:
            return 
        if root.left:
            self.inorder(root.left, ans)
        ans.append(root.val)
        if root.right:
            self.inorder(root.right, ans)
