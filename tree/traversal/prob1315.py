class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        cur = [root]
        ans = 0
        while cur:
            node = cur.pop(0)
            ans += self.helper(node)
            if node.left:
                cur.append(node.left)
            if node.right:
                cur.append(node.right)
                
        return ans
            
        
    def helper(self, node):
        if not node:
            return 0
        if node.val % 2 == 1:
            return 0
        
        tot = 0
        if node.left:
            if node.left.left:
                tot += node.left.left.val
            if node.left.right:
                tot += node.left.right.val
                
        if node.right:
            if node.right.left:
                tot += node.right.left.val
            if node.right.right:
                tot += node.right.right.val
                
        return tot
