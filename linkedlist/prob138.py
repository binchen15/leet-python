# 138 Copy List with Random Pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return None

        head2 = Node(head.val)
        cur = head
        cur2 = head2

        hmap = {cur:cur2}

        while cur.next:
            cur2.next = Node(cur.next.val)
            cur = cur.next
            cur2 = cur2.next
            hmap[cur] = cur2

        cur = head
        cur2 = head2
        while cur:
            if cur.random:
                cur2.random = hmap[cur.random]
            cur = cur.next
            cur2 = cur2.next


        return head2
