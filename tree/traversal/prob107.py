# level order traversal, bottom up

class Solution(object):
    def levelOrderBottom(self, root):
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
                node = currL.pop(0)
                vals.append(node.val)
                if node.left:
                    nextL.append(node.left)
                if node.right:
                    nextL.append(node.right)
            ans.insert(0, vals)
            currL = nextL
            nextL = []
        return ans
            
        
