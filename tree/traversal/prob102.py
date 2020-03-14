# 102 level order traversal. via 2 queues
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        currL = [root]
        nextL = []
        ans   = []
        while currL:
            vals = []
            while currL:
                node = currL.pop(0)  # first element
                vals.append(node.val)
                if node.left:
                    nextL.append(node.left)
                if node.right:
                    nextL.append(node.right)
            ans.append(vals)
            currL = nextL
            nextL = []
        return ans
        
      
