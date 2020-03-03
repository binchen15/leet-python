# linked list even-ordd partition
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or \
           not head.next.next:
            return head
        
        odd  = head       # even branch 
        even = head.next  # odd branch
        h1   = odd 
        h2   = even
        while h1 and h2 and h2.next:
            h1.next = h2.next
            h2.next = h1.next.next
            h1 = h1.next
            h2 = h2.next
        h1.next = even
        return odd
