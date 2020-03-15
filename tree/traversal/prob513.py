# return the val of the first node of the last level
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        currL = [root]
        nextL = []
        while True: #?
            val = currL[0].val # this might be the return val
            while currL:       # construct the next level
                node = currL.pop(0)
                if node.left:
                    nextL.append(node.left)
                if node.right:
                    nextL.append(node.right)
            if nextL:  # there is anther level
                currL = nextL
                nextL = []
            else:
                return val
        return None    # should not happen
                    
                
                
        
