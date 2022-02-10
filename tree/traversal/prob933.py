class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        if root.val == x or root.val == y:
            return False
        
        cur = [root]
        nxt = []
        vals = []
        
        while True:
            while cur:
                node = cur.pop(0)
                if node.left:
                    nxt.append(node.left)
                    vals.append(node.left.val)
                if node.right:
                    nxt.append(node.right)
                    vals.append(node.right.val)
            
                if node.left and node.right:
                    if set([node.left.val, node.right.val]) == set([x,y]):
                        return False # same parent
            if not nxt:
                break
            else:
                if x in vals and y in vals:
                    return True
                if x in vals and y not in vals:
                    return False
                if y in vals and x not in vals:
                    return False
                cur = nxt
                nxt = []
                vals = []
                
        return False
