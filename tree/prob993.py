class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
 
        if root.val == x or root.val == y:
            return False

        parentX = self.findParent(root, 0, x)
        parentY = self.findParent(root, 0, y)

        if parentX[0] != parentY[0] and parentX[1] == parentY[1]:
            return True
        else:
            return False

    def findParent(self, root, level, val):

        if not root:
            return False

        if root.left:
            if root.left.val == val:
                return (root, level)
            else:
                tmp = self.findParent(root.left, level+1, val)
                if tmp:
                    return tmp
        if root.right:
            if root.right.val == val:
                return (root, level)
            else:
                tmp = self.findParent(root.right, level+1, val)
                if tmp:
                    return tmp

        return False
