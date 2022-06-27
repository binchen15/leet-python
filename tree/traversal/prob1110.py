class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        self.ans = []
        to_delete = set(to_delete)
        
        def helper(node, parent_deleted):
            if not node:
                return None
            
            if node.val in to_delete:
                helper(node.left, True)
                helper(node.right, True)
                return None
            else: # not delete current node
                if parent_deleted:
                    self.ans.append(node)
                node.left = helper(node.left, False)
                node.right = helper(node.right, False)
                return node
                
        helper(root, True)
        
        return self.ans
