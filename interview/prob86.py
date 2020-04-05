# 86. Partition List

# 15% solution
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        if head.val < x:
            head_l = head
            tail_l = head
            head_r = head.next
            while head_r and head_r.val < x:
                head_r = head_r.next
            tail_r = head_r # might both be none
        else:   
            head_r = head
            tail_r = head
            head_l = head.next
            while head_l and head_l.val >= x:
                head_l = head_l.next
            tail_l = head_l # might both be none
        
        if not head_r or not head_l:
            return head # no need of partition
        
        #prev = head
        curr = head.next
        while curr:
            v = curr.val
            if v < x: # left branch
                if curr != tail_l:
                    tail_l.next = curr
                    tail_l = tail_l.next
            else: # right branch
                if curr != tail_r:
                    tail_r.next = curr
                    tail_r = tail_r.next
            curr = curr.next
        tail_l.next = head_r
        tail_r.next = None
        return head_l
                
                 
