# first solution based on recursion 45%

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        if l1.val <= l2.val:
            head = l1
            ans = self.mergeTwoLists(l1.next, l2)
        else:
            head = l2
            ans = self.mergeTwoLists(l1, l2.next)
        head.next = ans
        return head

# double pointers solution.
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        if l1.val > l2.val:
            l1, l2 = l2, l1   # switch them
        # l1 always has the smallest element
        #  make senses to merge whole l2 onto l1
        
        ptr1 = l1
        ptr2 = l2
        
        while ptr2 != None:
            while ptr1.next and ptr1.next.val <= ptr2.val:
                ptr1 = ptr1.next
            # dest.next first bigger, or None
            new  = ptr1.next   # memorize it
            new2 = ptr2.next
            ptr1.next = ptr2  # insert the node
            ptr2.next = new
            ptr2 = new2
            ptr1 = ptr1.next
            
        return l1
 
       
