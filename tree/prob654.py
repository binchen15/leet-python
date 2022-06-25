class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums:
            return None
        
        imax = nums.index(max(nums))
        
        root = TreeNode(nums[imax])
        
        root.left = self.constructMaximumBinaryTree(nums[:imax])
        root.right = self.constructMaximumBinaryTree(nums[imax+1:])
        return root
