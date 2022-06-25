class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        n = len(preorder)
        if n == 1:
            return root
        i = 1
        while i < n and preorder[i] < preorder[0]:
            i += 1
            
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        
        return root
        
