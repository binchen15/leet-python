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

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        def findLength(node):
            cur = node
            n = 0
            while cur:
                n += 1
                cur = cur.next
            return n

        n = findLength(head)
        mid = n // 2

        cur = head
        i = 0
        while i < mid:
            cur = cur.next
            i += 1

        return cur

