class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        ans = []
        
        def walk(path, node):
            if not node:
                return
            
            if path:
                path += f"->{node.val}"
            else:
                path = f"{node.val}"
            if not node.left and not node.right:
                ans.append(path)
                return
            if node.left:
                walk(path, node.left)
            if node.right:
                walk(path, node.right)
                
        walk("", root)
        
        return ans
