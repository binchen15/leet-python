# postorder traversal
# left, right, root

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.traversal(root, ans)
        return ans
        
    def traversal(self, root, ans):
        if not root:
            return
        if root.left:
            self.traversal(root.left, ans)
        if root.right:
            self.traversal(root.right, ans)
        ans.append(root.val)
