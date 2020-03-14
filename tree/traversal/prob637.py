# 637 average of levels of binary tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root == None:
            return []
        currL = [root]  # queue store nodes of current level
        nextL = []      # next level, alternating with currL
        ans   = []      # store avg of each level
        while currL:
            tot = 0     # sum of current level
            cnt = 0     # count of current level
            while currL:
                node = currL.pop(0)
                tot += node.val
                cnt += 1
                if node.left:
                    nextL.append(node.left)
                if node.right:
                    nextL.append(node.right)
            avg = tot/float(cnt)
            ans.append(avg)  # done with current level
            currL = nextL    # switch
            nextL = []
        return ans            
            
