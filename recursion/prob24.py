# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        nxt = head.next  # new head
        
        tmp = nxt.next
        nxt.next = head
        head.next = self.swapPairs(tmp)
        
        return nxt
