class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def helper(node, depth):
            """return max depth of leaves, 
            and subtree of node contains all those deepest leaves of the max depth"""
            if not node:
                return depth, None
            
            max_l, sub_l = helper(node.left, depth+1)
            max_r, sub_r = helper(node.right, depth+1)
            
            if max_l == max_r:
                return max_l, node
            elif max_l > max_r:
                return max_l, sub_l
            else:
                return max_r, sub_r
            
        m, node = helper(root, 0)
        
        return node
