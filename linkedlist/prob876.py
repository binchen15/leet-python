# 876 Middle of the linked list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        l = 0 # length
        curr = head
        while curr:
            l += 1
            curr = curr.next

        m = l // 2
        i = 0
        curr = head
        while i < m:
            curr = curr.next
            i   += 1
        return curr

