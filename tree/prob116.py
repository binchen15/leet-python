class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return root
    
        root.next = None
        
        if not root.left:
            return root
            
        left = self.connect(root.left)
        right = self.connect(root.right)
        
        self.joinLeftToRight(left, right)
        
        return root
    
    def joinLeftToRight(self, left, right):
        cur1 = left
        cur2 = right
        while cur1:
            cur1.next = cur2
            cur1 = cur1.right
            cur2 = cur2.left
