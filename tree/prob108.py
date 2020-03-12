# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        m = len(nums)
        if m == 1:
            return TreeNode(nums[0])
        if m == 2:
            root = TreeNode(nums[1])
            left = TreeNode(nums[0])
            root.left = left
            return root
        mid   = m // 2
        root  = TreeNode(nums[mid])
        left  = self.sortedArrayToBST(nums[:mid])
        right = self.sortedArrayToBST(nums[mid+1:])
        root.left = left
        root.right = right
        return root
        
