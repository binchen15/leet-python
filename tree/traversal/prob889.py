class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        
        m = len(preorder)
        if m == 1:
            return root
        
        preorder = preorder[1:]
        postorder = postorder[:-1]
        
        lhead = preorder[0]
        lb = postorder.index(lhead)
        
        preL = preorder[:lb+1]
        preR = preorder[lb+1:]
        
        postL = postorder[:lb+1]
        postR = postorder[lb+1:]
        
        root.left = self.constructFromPrePost(preL, postL)
        root.right = self.constructFromPrePost(preR, postR)
        
        return root
        
