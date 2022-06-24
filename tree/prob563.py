class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        tilts = []
        def walk(root):
            if not root:
                return
            l, r = self.helper(root.left), self.helper(root.right)
            tilts.append(abs(r-l))
            if root.left:
                walk(root.left)
            if root.right:
                walk(root.right)
        
        walk(root)
        return sum(tilts)
         
    def helper(self, root):
        if not root:
            return 0
        return root.val + self.helper(root.left) + self.helper(root.right)

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        tilts = [0]
        def walk(root):
            if not root:
                return
            l, r = self.helper(root.left), self.helper(root.right)
            tilts[0] += abs(r-l)
            if root.left:
                walk(root.left)
            if root.right:
                walk(root.right)
        
        walk(root)
        return tilts[0]
        
        
        
    @lru_cache
    def helper(self, root):
        if not root:
            return 0
        
        return root.val + self.helper(root.left) + self.helper(root.right)

# post-order traversal
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        self.answer = 0
        self.helper(root)

        return self.answer

    def helper(self, root):
        if not root:
            return 0
        l, r = self.helper(root.left),  self.helper(root.right)
        self.answer += abs(r-l)
        return l + r + root.val
