class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        cur = [root]
        nxt = []
        
        while True:
            tot = 0
            while cur:
                node = cur.pop(0)
                tot += node.val
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
                    
            if not nxt:
                return tot
            else:
                cur = nxt
                nxt = []
                
