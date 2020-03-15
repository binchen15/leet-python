# 144 preorder Traversal 
# root, left, right
class Solution(object):
    def preorderTraversal(self, root):
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
        ans.append(root.val)
        if root.left:
            self.traversal(root.left, ans)
        if root.right:
            self.traversal(root.right, ans)
            
        
