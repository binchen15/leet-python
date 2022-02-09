class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        
        if not node:
            return None
        
        if node.right:
            return self.findMin(node.right)
         
        p = node.parent
        if not p:
            return None
        
        while p.val < node.val and p.parent:
            p = p.parent
            
        if p.val > node.val:
            return p
        else:
            return None
        
            
    def findMin(self, node):
        """assume node is not None"""
        cur = node
        while cur.left:
            cur = cur.left
        return cur
