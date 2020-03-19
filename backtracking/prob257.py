# 257 Binary tree paths

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        
        results = []
        parts   = [str(root.val)]
        self.traverse(parts, root, results)
        return results
    
    def traverse(self, parts, node, results):
        """the node.val already in parts[-1]"""
        if not node.left and not node.right: # leaf node
            results.append("->".join(parts))
            return
        if node.left:
            parts.append(str(node.left.val))
            self.traverse(parts, node.left, results)
            parts.pop()
        if node.right:
            parts.append(str(node.right.val))
            self.traverse(parts, node.right, results)
            parts.pop()


