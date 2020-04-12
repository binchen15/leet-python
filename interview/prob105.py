# 105 Construct Binary Tree from Preorder and inorder traversal

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        m = len(preorder)
        if not m:
            return None
        root = TreeNode(preorder[0])
        if m == 1:
            return root
        idx = inorder.index(preorder[0])
        pre_left   = preorder[1:idx+1]
        pre_right  = preorder[idx+1:]
        in_left    = inorder[:idx]
        in_right   = inorder[idx+1:]
        root.left  = self.buildTree(pre_left, in_left)
        root.right = self.buildTree(pre_right, in_right)
        return root
        
