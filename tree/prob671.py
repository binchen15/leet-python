# 671. Find second minum of a special binary tree

# 70% performance
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        if not root.left: # which means not root.right too
            return -1

        # root has two children
        if root.left.val < root.right.val:
            l = self.findSecondMinimumValue(root.left)
            if l == -1:
                return root.right.val
            else:
                return min(l, root.right.val)
        elif root.left.val > root.right.val:
            r = self.findSecondMinimumValue(root.right)
            if r == -1:
                return root.left.val
            else:
                return min(root.left.val, r)
        else:
            l = self.findSecondMinimumValue(root.left)
            r = self.findSecondMinimumValue(root.right)
            if l == -1 and r == -1:
                return -1
            elif l == -1:
                return r
            elif r == -1:
                return l
            else:
                return min(l, r)

# 
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        vals = set()

        if not root:
            return -1

        cur = [root]
        while cur:
            node = cur.pop(0)
            if node.val not in vals:
                    vals.add(node.val)
            if node.left:
                cur.extend([node.left, node.right])

        if len(vals) == 1:
            return -1

        return sorted(vals)[1]

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return -1
        
        min1 = root.val
        min2 = sys.maxsize
        
        cur = [root]
        while cur:
            node = cur.pop(0)
            v = node.val
            if min1 < v < min2:
                min2 = v
                # no need to track children of min2
            elif min1 == v and node.left:
                cur.extend([node.left, node.right])
            
                
        if min2 == sys.maxsize:
            return -1
        return min2
        
