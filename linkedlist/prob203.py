class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ans = head
        while ans and ans.val == val:
            ans = ans.next
        if not ans or not ans.next:
            return ans  # nothing to do
        
        curr = ans  # curr not None, and curr.val != val
        while True:
            # move to a good node whose next node is bad
            while curr.next and curr.next.val != val:
                curr = curr.next 
            if not curr.next:
                break
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next # remove a node
            if not curr.next:
                break
            curr = curr.next
        return ans
            
        
