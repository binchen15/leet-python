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

# O(n) but only iterate only once
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

        while cur:
            if cur.next:
                if cur.next in hmap:
                    cur2.next = hmap[cur.next]
                else:
                    cur2.next = Node(cur.next.val)
                    hmap[cur.next] = cur2.next
            if cur.random:
                if cur.random not in hmap:
                    cur2.random = Node(cur.random.val)
                    hmap[cur.random] = cur2.random
                else:
                    cur2.random = hmap[cur.random]
            cur = cur.next
            cur2 = cur2.next

        return head2

# copy graph solution recursion
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        visited = {}

        def copy_graph(head):
            if not head:
                return None
            if head in visited:
                return visited[head]

            new_head = Node(head.val)
            visited[head] = new_head
            new_head.next = copy_graph(head.next)
            new_head.random = copy_graph(head.random)
            return new_head

        return copy_graph(head)

