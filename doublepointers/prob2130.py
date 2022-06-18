# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next

        ans = 0
        l, r = 0, len(vals)-1
        while l < r:
            ans = max(ans, vals[l] + vals[r])
            l += 1
            r -= 1
            
        return ans
