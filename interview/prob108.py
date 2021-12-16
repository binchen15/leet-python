# 108 Sorted Array to Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        n = len(nums)

        def helper(i, j):
            "convert nums[i:j+1]"
            if i > j:
                return None
            elif i == j:
                return TreeNode(nums[i])
            elif i == j - 1:
                root = TreeNode(nums[i])
                right = TreeNode(nums[i+1])
                root.right = right
                return root
            else:
                mid = (i+j)//2
                root = TreeNode(nums[mid])
                root.left = helper(i, mid-1)
                root.right = helper(mid+1, j)
                return root

        return helper(0, n-1)
