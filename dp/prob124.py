class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        self.ans = -sys.maxsize
        
        def walk(node):
            if not node:
                return 0
            self.ans = max(self.ans, self.helper(node))
            if node.left:
                walk(node.left)
            if node.right:
                walk(node.right)
             
        walk(root)
        
        return self.ans
            
    @lru_cache(maxsize=None)    
    def helperLeft(self, node):
        """max path sum from node, down to its left subtree?"""
        
        if not node:
            return 0
        
        ans = node.val
        if not node.left:
            return ans
        
        l = self.helperLeft(node.left)
        r = self.helperRight(node.left)
        if max(l, r) <= 0:
            return ans
        else:
            return ans + max(l, r)
        
    @lru_cache(maxsize=None)  
    def helperRight(self, node):
        """max path sum from node, down to its right subtree?"""
        
        if not node:
            return 0
        
        ans = node.val
        if not node.right:
            return ans
        
        l = self.helperLeft(node.right)
        r = self.helperRight(node.right)
        if max(l, r) <= 0:
            return ans
        else:
            return ans + max(l, r)
            
    @lru_cache(maxsize=None)         
    def helper(self, node):
        """math path sum pass through node"""
        if not node:
            return 0
        l, r = self.helperLeft(node), self.helperRight(node)
        return l + r - node.val
