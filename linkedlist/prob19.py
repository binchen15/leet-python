# remove Nth from the end of singly-linked list

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return head

        curr  = head
        nodes = []
        while curr != None:
            nodes.append(curr)
            curr = curr.next

        m = len(nodes)
        if n > m:
            return head

        if n == m: # remove the first
            return head.next

        nodes[m-n-1].next = nodes[m-n].next
        return nodes[0]
