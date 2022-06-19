class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def helper(head):
            """"find length of list"""
            cur = head
            size = 0
            while cur:
                size += 1
                cur = cur.next 
            return size
            
        n = helper(head)
        if n <= 1:
            return head
        if k - 1 == n - k: # same nodes to swap
            return head
        
        first, second = min(k-1, n-k), max(k-1, n-k)
        
        i = 0
        cur = head
        while cur:
            if i == first:
                n1 = cur
            elif i == second:
                n2 = cur
                break
            i += 1
            cur = cur.next
            
        n1.val, n2.val = n2.val, n1.val
        
        return head
