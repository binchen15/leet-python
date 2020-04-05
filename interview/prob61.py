# 61. Rotate List

# traverse the list twice...
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        m = 0 # length of the list
        curr = head
        while curr:
            m += 1
            curr = curr.next
            
        k = k % m # save some work
        if not k:
            return head
        
        curr = head
        for _ in range(m-k-1):
            curr = curr.next
            
        new_head = curr.next
        tail     = new_head
        curr.next = None
        while tail.next:
            tail = tail.next
        tail.next = head
        return new_head
            
            
