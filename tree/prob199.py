class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        ans = []
        cur = [root]
        nxt = []
        
        while True:
            vals = []
            while cur:
                node = cur.pop(0)
                vals.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)

            ans.append(vals[-1])
            if nxt:
                cur = nxt
                nxt = []
                vals = []
            else:
                break
                
        return ans
