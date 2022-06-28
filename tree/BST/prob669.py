# prob. 669 trim BST [L, R]

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val > R:
            return self.trimBST(root.left,  L, R)
        if root.val < L:
            return self.trimBST(root.right, L, R)
        # root \in [L, R]
        root.left  = self.trimBST(root.left,  L, R)
        root.right = self.trimBST(root.right, L, R)
        return root

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        if not root:
            return None

        if root.val < low:
            r = root.right
            root.right = None
            return self.trimBST(r, low, high)
        if root.val == low:
            root.left = None
            root.right = self.trimBST(root.right, low, high)
            return root

        if root.val > high:
            l = root.left
            root.left = None
            return self.trimBST(l, low, high)

        if root.val == high:
            root.right = None
            root.left = self.trimBST(root.left, low, high)
            return root

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
