class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        memo = []
        
        def walk(root):
            if root.right:
                walk(root.right)
            if not memo:
                memo.insert(0, root.val)
            else:
                memo.insert(0, root.val+memo[0]) 
            if root.left:
                walk(root.left)
        
        walk(root)
        
        self.cnt = 1 # memo[0] not used..
        
        def walk2(root):
            if root.left:
                walk2(root.left)
            if self.cnt < len(memo):
                root.val += memo[self.cnt]
                self.cnt += 1
            if root.right:
                walk2(root.right)
                
        walk2(root)
        
        return root
