class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
                
        def walk(root):    
            if not root:
                return []
            return walk(root.left) + [root.val] + walk(root.right)
        
        vals = walk(root)
        
        n = len(vals)
        ans = vals[1] - vals[0]
        
        for i in range(1, n-1):
            ans = min(ans, vals[i+1]-vals[i])
            
        return ans
