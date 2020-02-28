# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        slow = head
        fast = head.next
        while slow != None and fast != None and fast.next != None:
            if slow == fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        return False
        
