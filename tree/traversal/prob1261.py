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

# find path, slighter faster then brute force finding
class FindElements:

    def __init__(self, root: Optional[TreeNode]):

        self.root = root
        if root:
            self.root.val = 0
            self.recover(self.root)

    def recover(self, root):
        """assume root.val is already recovered"""

        if not root:
            return
        if root.left:
            root.left.val = 2 * root.val + 1
            self.recover(root.left)
        if root.right:
            root.right.val = 2 * root.val + 2
            self.recover(root.right)


    def helper2(self, target):
        ans = [target]
        while target > 0:
            target = (target - 1) // 2
            ans.insert(0, target)

        return ans

    def helper3(self, node, path, i):
        print(i, path[i], node.val, path)
        if i == len(path):
            return True
        if not node:
            return False
        if node.val != path[i]:
            return False
        if i == len(path) - 1:
            return True
        if node.left and node.left.val == path[i+1]:
            return self.helper3(node.left, path, i+1)

        if node.right and node.right.val == path[i+1]:
            return self.helper3(node.right, path, i+1)

        return False


    def find(self, target: int) -> bool:

        path = self.helper2(target)
        return self.helper3(self.root, path, 0)
