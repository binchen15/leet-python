# 92 Reverse Linked List II

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        """prev->tail(m)->....minus->curr... in the end"""
        if not head:
            return None
        if not head.next:
            return head
        if n == 1:
            return head
        
        prev = None
        curr = head
        cnt  = 1
        while cnt < m:
            prev = curr
            curr = curr.next
            cnt += 1
        
        minus = None
        tail  = curr
        while cnt <= n:
            tmp = curr.next
            curr.next = minus
            minus = curr
            curr = tmp
            cnt += 1
        
        tail.next = curr
        if prev:
            prev.next = minus
        else: # m == 1
            head = minus
        
        return head
