class Solution(object):
    """5% recursion solution."""
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        # a shorter list
        reverse = self.reverseList(head.next)
        curr = reverse
        while curr.next != None:
            curr = curr.next
        curr.next = head
        head.next = None  # line critical
        return remain_reversed
        
class Solution(object):
    """69% recursion solution"""
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or \
           head.next == None:
            return head
        
        # a shorter list
        scnd    = head.next
        reverse = self.reverseList(scnd)
        scnd.next = head
        head.next = None
        return reverse
        
class Solution(object):
    """69% iteration solution"""
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or \
           head.next == None:
            return head
        
        l    = []     # use python list as a stack
        curr = head
        while curr != None: 
            l.append(curr)
            curr = curr.next
        rev  = l.pop()  # tail becomes new head
        prev = rev
        while l:
            n = l.pop()
            prev.next = n
            prev = n
        prev.next = None
        return rev
	
class Solution(object):
    """40% solution"""
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or \
           head.next == None:
            return head
        
        l    = []     # use python list as a stack
        curr = head
        while curr != None: 
            l.append(curr)
            curr = curr.next
        m = len(l)
        for i in range(m-1):
            l[m-1-i].next = l[m-2-i]
        l[0].next = None
        return l[-1]
        
    
