#The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node
# note: null node is not a leaf node

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            if root.left and root.right:
                return 1 + min(
                    self.minDepth(root.left),
                    self.minDepth(root.right)
                )
            elif root.left:
                return 1 + self.minDepth(root.left)
            elif root.right:
                return 1 + self.minDepth(root.right)
            else:
                return 1

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        cur = [root]
        nxt = []
        depth = 1
        while True:
            while cur:
                node = cur.pop(0)
                if not node.left and not node.right:
                    return depth
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            
            cur = nxt
            nxt = []
            depth += 1
