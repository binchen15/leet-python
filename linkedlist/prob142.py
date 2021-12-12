class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        def hasCycle(head):
            if not head:
                return False
            cur1 = head
            cur2 = head.next
            if not cur2:
                return False
            
            while cur2:
                if cur1 == cur2:
                    return True
                if not cur2.next:
                    return False
                else:
                    cur2 = cur2.next.next
                    cur1 = cur1.next
            return False
                
        
        def findCycleNode(head):
            visited = set()
            cur = head
            while cur:
                if cur in visited:
                    return cur
                else:
                    visited.add(cur)
                    cur = cur.next
        
        
        if not hasCycle(head):
            return None
        else:
            return findCycleNode(head)

