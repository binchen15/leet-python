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
