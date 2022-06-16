# 143 reorder list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        n = self.size(head)
        if n <= 2:
            return

        m = (n-1) // 2  # tail of first half

        i = 0
        cur = head
        while i < m:
            cur = cur.next
            i += 1

        tmp = cur.next
        cur.next = None  # cut the first half

        l2 = self.reverse(tmp)
        self.merge(head, l2, n // 2)


    def size(self, head):
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n += 1
        return n

    def reverse(self, head):

        if not head or not head.next:
            return head

        tmp = head.next
        head.next = None

        ans = self.reverse(tmp)
        tmp.next = head
        return ans

    def merge(self, l1, l2, m):

        i = 0
        c1, c2 = l1, l2
        while i < m:
            n1 = c1.next
            n2 = c2.next
            c1.next = c2
            c2.next = n1
            c1 = n1
            c2 = n2
            i += 1

