# inorder traversal
# left, root, right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.traversal(root, ans)
        return ans
    
    def traversal(self, root, ans):
        if root == None:
            return
        if root.left:
            self.traversal(root.left, ans)
        ans.append(root.val)
        if root.right:
            self.traversal(root.right, ans)
            
            
