class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return None
        
        root.next = None
        
        self.connect(root.left)
        self.connect(root.right)
        
        if not root.left or not root.right:
            return root
        
        l1 = self.helper(root.left, True)
        l2 = self.helper(root.right, False)
        
        n = min(len(l1), len(l2))
        for i in range(n):
            l1[i].next = l2[i]
            
        return root
    
    def helper(self, root, flag):
        """level order traversal, return right most element of each layer"""
        ans = []
        if not root:
            return ans
        
        ans.append(root)
        cur = [root]
        nxt = []
        
        while True:
            while cur:
                node = cur.pop(0)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            if not nxt:
                break
            else:
                if flag:
                    ans.append(nxt[-1])
                else:
                    ans.append(nxt[0])
                cur = nxt
                nxt = []
                
        return ans

