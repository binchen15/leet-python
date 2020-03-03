class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        new_head = head.next  # must be the 2nd node
        curr = head
        prev = None
        while curr and curr.next:
            if prev:
                prev.next = curr.next
            tail_node = curr.next.next
            curr.next.next = curr
            curr.next = tail_node
            prev = curr
            curr = curr.next
        return new_head
            
