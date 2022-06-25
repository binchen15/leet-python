# 1261 with memoization
class FindElements:

    def __init__(self, root: Optional[TreeNode]):

        self.root = root
        self.vals = set()
        if root:
            self.vals.add(0)
            self.root.val = 0
            self.recover(self.root)


    def recover(self, root):
        """assume root.val is already recovered"""

        if not root:
            return
        if root.left:
            root.left.val = 2 * root.val + 1
            self.vals.add(root.left.val)
            self.recover(root.left)
        if root.right:
            root.right.val = 2 * root.val + 2
            self.vals.add(root.right.val)
            self.recover(root.right)

    def helper(self, node, target):

        if not node:
            return False
        if node.val == target:
            return True

        return self.helper(node.left, target) or self.helper(node.right, target)


    def find(self, target: int) -> bool:

        return target in self.vals
        # return self.helper(self.root, target)

