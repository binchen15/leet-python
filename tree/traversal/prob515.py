class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        arr = []
        cur = [root]
        nxt = []
        
        while True:
            
            tmp = -sys.maxsize
            while cur:
                node = cur.pop(0)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)    
                tmp = max(tmp, node.val)  
            arr.append(tmp)
            if nxt:
                cur = nxt
                nxt = []
            else:
                break
                
        return arr
