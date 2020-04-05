# 82 Remove Duplicates from Sorted List II

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        # find a good start (need a while loop not if here)
        while head and head.next and head.val == head.next.val:
            v = head.val
            while head and head.val == v:
                head = head.next
                
        if not head or not head.next:
            return head       
        
        # head is not None, and is not duplicates, with next node
        
        prev = head
        curr = head.next 
        while curr:
            if not curr.next or curr.next.val != curr.val:
                prev = curr
                curr = curr.next
            else:
                v = curr.val
                while curr and curr.val == v:
                    curr = curr.next
                prev.next = curr # None, or a new-value node
        
        return head
        

