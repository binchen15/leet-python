# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:

        if not s:
            return None
        elif "(" not in s:
            return TreeNode(int(s))

        root_str, left_str, right_str = self.helper(s)
        root = TreeNode(int(root_str))
        root.left = self.str2tree(left_str)
        root.right = self.str2tree(right_str)
        return root

    def helper(self, s):
        """
        break s into three pieces, root, left, right,
        assume at least 1 pair of parenthesis exists
        """

        l = s.index("(")
        n = len(s)
        stack = 1
        for i in range(l+1,n):
            if s[i] == "(":
                stack += 1
            elif s[i] == ")":
                stack -= 1
                if stack == 0:
                    r = i
                    break
        root = s[:l]
        left = s[l+1:r]
        right = s[r+2:n-1]
        return (root, left, right)
