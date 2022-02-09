class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        l = self.inOrder(root)
        
        if target <= l[0]:
            return l[0]
        if target >= l[-1]:
            return l[-1]
        
        i = 0
        n = len(l)
        while i+1 < n and l[i+1] < target:
            i += 1
        d1 = target - l[i]
        d2 = l[i+1] - target
        if d1 <= d2:
            return l[i]
        else:
            return l[i+1]
        
    def inOrder(self, root) -> list:
        if not root:
            return []
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)

