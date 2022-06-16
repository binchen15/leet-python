# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        if n % 2 == 0:
            return []
        
        if n == 1:
            return [TreeNode(0)]
        
        ans = []
        
        for m in range(1, n-1, 2):
            left = self.allPossibleFBT(m)
            right = self.allPossibleFBT(n-1-m)
            
            for i in left:
                for j in right:
                    root = TreeNode(0)
                    root.left = i
                    root.right = j
                    ans.append(root)
                    
        return ans

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        return self.helper(n)

    def helper(self, n, memo={}):

        if n % 2 == 0:
            return []

        if n == 1:
            return [TreeNode(0)]

        if n in memo:
            return memo[n]

        ans = []

        for m in range(1, n-1, 2):
            left = self.helper(m, memo)
            right = self.helper(n-1-m, memo)

            for i in left:
                for j in right:
                    root = TreeNode(0)
                    root.left = i
                    root.right = j
                    ans.append(root)

        memo[n] = ans
        return ans
