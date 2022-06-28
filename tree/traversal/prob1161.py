class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        self.record  = -sys.maxsize
        self.holders = []
        cur = [root]
        nxt = []
        level = 1
        
        while True:
            tot = 0
            while cur:
                node = cur.pop(0)
                tot += node.val
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            if tot > self.record:
                self.record = tot
                self.holders = [level]
                
            if nxt:
                cur = nxt
                nxt = []
                level += 1
            else:
                break
                
        return self.holders[0]
