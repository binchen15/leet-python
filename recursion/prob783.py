# 783 Minimum Distance between BST nodes

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        arr = self.getArray(root)
        n = len(arr)
        if n < 2:
            return 0
        ans = arr[-1] - arr[0]
        for i in range(n-1):
            if arr[i+1] - arr[i] < ans:
                ans = arr[i+1] - arr[i]
        return ans

    def getArray(self, root): # in order traversal
        if not root:
            return []
        else:
            return self.getArray(root.left) + [root.val] + \
                    self.getArray(root.right)
