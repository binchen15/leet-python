# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        values = self.helper(root)     
        val1, val2 = self.findValues(values)
        
        n1 = self.findNode(root, val1)
        n2 = self.findNode(root, val2)

        n1.val, n2.val = n2.val, n1.val
        
    def helper(self, root):
        if not root:
            return []
        else:
            return self.helper(root.left) + [root.val] + self.helper(root.right)
        
    def findValues(self, values):
        
        n = len(values)
        s = sorted(values)
        ans = []
        
        for i in range(n):
            if values[i] != s[i]:
                ans = [values[i], s[i]]
                break
                    
        return ans
    
    def findNode(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        return self.findNode(root.left, val) or self.findNode(root.right, val)

