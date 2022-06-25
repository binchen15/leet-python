class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def inorder(root, ans):
            if not root:
                return
            if root.left:
                inorder(root.left, ans)
            ans.append(root.val)
            if root.right:
                inorder(root.right, ans)
            
        vals1 = []
        vals2 = []
        inorder(root1, vals1)
        inorder(root2, vals2)
        
        return sorted(vals1 + vals2)
